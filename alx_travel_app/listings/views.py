from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer
from .permissions import IsOwnerOrReadOnly


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["price_per_night", "bedrooms", "bathrooms"]
    search_fields = ["title", "description", "address"]
    ordering_fields = ["price_per_night", "created_at"]
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(host=self.request.user)


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["listing", "start_date", "end_date", "status"]
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
