from blog.api.viewsets import userviewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('blog', userviewsets, basename ='user_api')