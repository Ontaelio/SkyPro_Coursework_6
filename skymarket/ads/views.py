from rest_framework import viewsets, pagination
from django_filters.rest_framework import DjangoFilterBackend

from ads.models import Ad, Comment
from ads.filters import AdTitleFilter
from ads.serializers import AdSerializer, CommentSerializer
from rest_framework.generics import ListAPIView


class CommentsPagination(pagination.PageNumberPagination):
    page_size = 200000


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdTitleFilter

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(author=self.request.user)


class MyAdsViewList(ListAPIView):
    serializer_class = AdSerializer


    def get_queryset(self):
        return Ad.objects.all().filter(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = CommentsPagination

    def get_queryset(self, *args, **kwargs):
        adid = self.kwargs['adid']
        queryset = Comment.objects.filter(ad__id=adid)
        return queryset

    def perform_create(self, serializer, *args, **kwargs):
        adid = self.kwargs['adid']
        serializer.save(author=self.request.user, ad=Ad.objects.get(pk=adid))


