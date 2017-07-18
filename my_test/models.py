from django.db import models
from django.utils.text import slugify
from django.conf import settings
# Create your models here.


def image_upload_to(instance, filename):
    name = instance.name
    slug = slugify(name)
    basename, file_extension = filename.split(".")
    new_filename = "%s.%s" %(slug, file_extension)
    return "profiles/%s/%s" %(slug, new_filename)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=80,blank=True, null=True)
    image = models.ImageField(upload_to=image_upload_to)

    def __str__(self):
        return self.name


