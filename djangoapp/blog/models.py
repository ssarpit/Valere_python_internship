import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# ------------------- CUSTOM USER -------------------
class CustomUser(AbstractUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.username

# ------------------- POST CATEGORY -------------------
class PostCategory(models.Model):
    title = models.CharField(max_length=75)
    meta_title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

# ------------------- POST -------------------
class Post(models.Model):
    post_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post_title = models.CharField(max_length=255)
    caption = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    total_comments = models.IntegerField(default=0)
    post_likes = models.IntegerField(default=0)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(PostCategory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.post_title

# ------------------- POST LIKE -------------------
class PostLike(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} liked {self.post}"

# ------------------- COMMENT -------------------
class Comment(models.Model):
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment_text = models.CharField(max_length=255)
    comment_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    mentioned_user = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL, related_name='mentions')

    def __str__(self):
        return self.comment_text[:50]

# ------------------- COMMENT LIKE -------------------
class CommentLike(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} liked a comment"

# ------------------- NOTIFICATION -------------------
class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notifications')
    tagged_id = models.IntegerField(null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return f"Notification for {self.user.username}"

# ------------------- EMAIL OTP -------------------
class EmailOTP(models.Model):
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {self.otp}"

# ------------------- BOOK (EXTRA FEATURE) -------------------

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publish_date = models.DateField()

  