from django.db import models
from django.conf import settings


class Company(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contacts = models.CharField(max_length=200)
    info = models.TextField()
    logo = models.ImageField(upload_to='logo', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'


class Post(models.Model):
    title = models.CharField(max_length=30)
    info = models.TextField()
    user_id = models.ForeignKey(Company, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField()
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)


class CompanyFavorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    company = models.ForeignKey(Company, related_name='is_favorite', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Избранная компания'
        verbose_name_plural = 'Избранные компании'

    def __str__(self):
        return self.company.name


class PostFavorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    post = models.ForeignKey(Post, related_name='is_favorite', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Избранный пост'
        verbose_name_plural = 'Избранные посты'

    def __str__(self):
        return self.post.name

