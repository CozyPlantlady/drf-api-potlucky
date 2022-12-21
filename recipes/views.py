from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Recipe
from .serializers import RecipeSerializer


class RecipeList(APIView):
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        recipe = Recipe.objects.all()
        serializer = RecipeSerializer(
            recipe, many=True, context={'request': request}
            )
        return Response(serializer.data)

    def post(self, request):
        serializer = RecipeSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
