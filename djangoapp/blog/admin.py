from django.contrib import admin
from .models import (
    CustomUser,
    PostCategory,
    Post,
    PostLike,
    Comment,
    CommentLike,
    Notification
)

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone_number', 'gender', 'dob', 'is_active']
    search_fields = ['username', 'email', 'phone_number']
    list_filter = ['is_active', 'gender']

@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'meta_title']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_title', 'user', 'category', 'date', 'total_comments', 'post_likes']

@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ['post', 'user', 'timestamp']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_text', 'user', 'post', 'comment_date', 'parent_comment', 'mentioned_user']

@admin.register(CommentLike)
class CommentLikeAdmin(admin.ModelAdmin):
    list_display = ['comment', 'user', 'post', 'date']

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'comment', 'tagged_id']
