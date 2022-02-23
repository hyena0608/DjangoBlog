from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200) 
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo')

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    # 외래키
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)