from django.db import models


class Ad(models.Model):
    title = models.CharField(unique=True, max_length=200)
    price = models.PositiveIntegerField()
    description = models.TextField()
    author = models.ForeignKey("users.User", on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="ad_images", null=True, blank=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['created_at']


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
