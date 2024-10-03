from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class BaseSlugModel(models.Model):
    name = models.CharField(max_length=255)  #yaxshi olam
    slug = models.SlugField(max_length=255, unique=True, editable=False) #yaxshi-olim

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        count = 0
        while self.__class__.objects.filter(slug=self.slug).exists():
            self.slug = f'_{count}'
            # yaxshi-olim_0_1
            count += 1
        super().save(*args, force_insert=force_insert, force_update=force_update, using=using,
                     update_fields=update_fields)

    class Meta:
        abstract = True


class Category(BaseSlugModel):

    def __str__(self):
        return self.name


class Menyu(BaseSlugModel):   # noqa
    about = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Comment(models.Model):
    about = models.TextField()
    rating = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Menyu, on_delete=models.CASCADE)



