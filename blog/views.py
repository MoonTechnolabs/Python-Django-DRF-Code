from rest_framework import generics, mixins
from rest_framework.exceptions import NotFound
from .models import Blog
from .serializers import BlogSerializer


class BlogView(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               generics.GenericAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        """
        Return blogs belonging to the authenticated user.
        """
        if self.request.user.is_authenticated:
            return Blog.objects.filter(author=self.request.user)
        return Blog.objects.none()

    def get_object(self):
        """
        Retrieve a specific blog by `pk` and ensure it belongs to the authenticated user.
        """
        queryset = self.get_queryset()
        obj = queryset.filter(pk=self.kwargs.get('pk')).first()
        if not obj:
            raise NotFound("No Blog matches the given query.")
        return obj

    def perform_create(self, serializer):
        """
        Automatically set the logged-in user as the author of the blog.
        """
        serializer.save(author=self.request.user)

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests for both list and retrieve actions.
        """
        if kwargs.get('pk'):  # Retrieve a single blog
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)  # List all blogs for the user

    def post(self, request, *args, **kwargs):
        """
        Handle POST request for creating a blog.
        """
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Handle PUT request for updating a blog.
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Handle DELETE request for deleting a blog.
        """
        return self.destroy(request, *args, **kwargs)
