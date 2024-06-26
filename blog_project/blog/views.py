from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer
from .models import Post

class PostListView(APIView):
    def get(self, request):
        """
        Handles the GET request for the list of posts.
        Retrieves all posts from the database, serializes them, and returns the serialized data.

        Args:
            request: The request object.

        Returns:
            A Response object with the serialized data of all posts.
        """
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Handles the POST request for creating a new post.
        Serializes and validates the data from the request. If valid, saves the new post to the database.

        Args:
            request: The request object.

        Returns:
            A Response object with the serialized data of the new post if the data is valid,
            otherwise returns the serialization errors.
        """
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class PostDetailView(APIView):
    def get_object(self, pk):
        """
        Retrieves a specific post by its primary key (pk).

        Args:
            pk: The primary key of the post.

        Returns:
            The Post object if it exists, otherwise None.
        """
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return None

    def get(self, request, pk):
        """
        Handles the GET request for a specific post.

        Retrieves the post by its primary key (pk), serializes it, and returns the serialized data.
        If the post does not exist, returns a message and a 404 status.

        Args:
            request: The request object.
            pk: The primary key of the post.

        Returns:
            A Response object with the serialized data of the post if it exists,
            otherwise a message and a 404 status.
        """
        post = self.get_object(pk)
        if post is not None:
            serializer = PostSerializer(post)
            return Response(serializer.data)
        return Response({'message': 'Post no encontrado'}, status=status.HTTP_404_NOT_FOUND)