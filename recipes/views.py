from django.http import Http404
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Recipe
from .serializers import RecipeSerializer
from potlucky_drf_api.permissions import IsOwnerOrReadOnly


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


class RecipeDetail(APIView):
    serializer_class = RecipeSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            recipe = Recipe.objects.get(pk=pk)
            self.check_object_permissions(self.request, recipe)
            return recipe
        except Recipe.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(recipe, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(recipe, data=request.data,
                                      context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        recipe = self.get_object(pk)
        recipe.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
