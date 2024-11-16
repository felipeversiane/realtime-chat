from django.db import models
import uuid
from django.contrib.auth import get_user_model

class Modifier(models.Model):
    id = models.UUIDField(
        default=uuid.uuid1, unique=True, primary_key=True, editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
class ChatGroup(Modifier):
    group_name = models.CharField(max_length=128, null=False, blank=False, unique=True)
    
    def __str__(self):
        return "{}".format(self.group_name)

class GroupMessage(Modifier):
    group = models.ForeignKey(ChatGroup,related_name='chat_messages',on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    
    def __str__(self):
        return "{} : {}".format(self.author.username, self.body)
    
    class Meta:
        ordering = ['created_at']