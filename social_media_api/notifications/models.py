from django.db import models
from accounts.models import CustomUser 
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Notification(models.Model):
    recipient = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name = 'receiver')
    actor = models.ForeignKey(CustomUser, on_delete = models.CASCADE, relate_name ='liker')
    verb = models.CharField(max_length = 255 )
    target_content_type = models.ForeignKey(ContentType, on_delete = models.CASCADE, related_name = 'posts-comments-follow')
    target_object_id = models.PositiveIntegerField(blank=True, null=True)
    target = GenericForeignKey(target_content_type , target_object_id) 
    timestamp = models.DateTimeField(auto_now_add = True)
    is_read = models.BooleanField(default=False)

# Create your models here.
