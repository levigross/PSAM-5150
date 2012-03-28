from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save

class ModelAudit(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Message(ModelAudit):
    title = models.CharField(max_length=100)
    message_content = models.TextField()
    recipient = models.ForeignKey(User, related_name="mb_messages")


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='UserProfile', unique=True)
    accepted_terms = models.BooleanField(default=False)
    is_hacked = models.BooleanField(default=False)


class LoginAuditLog(models.Model):
    user = models.ForeignKey(User, unique=True, related_name='audit_log', editable=False)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    ip_address = models.IPAddressField(editable=False)


    def delete(self, using=None, force=False):
        if force is True:
            super(LoginAuditLog, self).delete(using=using)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


def create_audit_record(sender, request, user, **kwargs):
    LoginAuditLog.objects.create(user=user, ip_address=request.META['REMOTE_ADDR'])


post_save.connect(create_user_profile, sender=User)
user_logged_in.connect(create_audit_record, sender=User)

