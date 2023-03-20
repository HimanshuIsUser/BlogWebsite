from django.db import models
from login.models import CustomUser
import uuid
from froala_editor.fields import FroalaField
from django.utils.text import slugify
from .helpers import generate_slug
# Create your models here.

class BlogModel(models.Model):
    id = models.UUIDField(primary_key=True,default = uuid.uuid4,editable=False)
    title = models.CharField(max_length=1000)
    content = FroalaField()
    slug = models.SlugField(max_length=1000,null=True,blank=True)
    image = models.ImageField(upload_to='blog')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser,null=True,blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def save(self,*args, **kwargs):
        self.slug = generate_slug(self.title)
        super(BlogModel,self).save(*args, **kwargs)