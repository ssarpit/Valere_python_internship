from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
# ------------------- USER / ADMIN -------------------
class CustomUser(AbstractUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)  # renamed from DOB
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    # keep rest as-is

# ------------------- POST CATEGORY -------------------
class PostCategory(models.Model):
    category_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=75)
    meta_title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

# ------------------- POST -------------------
class Post(models.Model):
    post_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    post_title = models.CharField(max_length=255)
    total_comments = models.IntegerField(default=0)
    post_likes = models.IntegerField(default=0)
    caption = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(PostCategory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.post_title

# ------------------- POST LIKE -------------------
class PostLike(models.Model):
    post_like_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

# ------------------- COMMENT -------------------
class Comment(models.Model):
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_text = models.CharField(max_length=255)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    mentioned_user = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL, related_name='mentions')

    def __str__(self):
        return self.comment_text[:50]

# ------------------- COMMENT LIKE -------------------
class CommentLike(models.Model):
    comment_like_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

# ------------------- NOTIFICATION -------------------
class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notifications')
    tagged_id = models.IntegerField(null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return f"Notification for {self.user.username}"
# models.py
import random

class EmailOTP(models.Model):
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {self.otp}"
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publish_date = models.DateField()

    def __str__(self):
        return self.title