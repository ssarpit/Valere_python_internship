from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser

from .models import (
    CustomUser,
    PostCategory,
    Post,
    PostLike,
    Comment,
    CommentLike,
    Notification,
    Book
)


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'phone_number', 'gender', 'dob', 'is_staff', 'is_superuser']
    search_fields = ['username', 'email', 'phone_number']
    list_filter = ['is_active', 'is_staff', 'gender']
    
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('phone_number', 'gender', 'dob')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone_number', 'gender', 'dob', 'password1', 'password2', 'is_staff', 'is_superuser')}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)

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

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['title','author','publish_date']