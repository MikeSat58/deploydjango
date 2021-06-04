from rest_auth.views import LogoutView
from rest_framework import permissions
from rest_framework import mixins, viewsets
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin

from blog_api import serializers
from blog_api.models import PostImages


class CustomLogoutView(LogoutView):
    permission_classes = (permissions.IsAuthenticated, )




class PostImagesViewSet(mixins.CreateModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    serializer_class = serializers.PostSerializer
    queryset = PostImages.objects.all()
