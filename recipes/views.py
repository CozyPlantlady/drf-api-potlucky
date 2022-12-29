from rest_framework import generics, permissions, filters
from .models import Recipe
from .serializers import RecipeSerializer
from potlucky_drf_api.permissions import IsOwnerOrReadOnly


class RecipeList(generics.ListCreateAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Recipe.objects.all()
    filter_backends = [
        filters.SearchFilter,
    ]
    search_fields = [
        'owner__username',
        'title',
        'keywords',
        'method',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Recipe.objects.all()
