from rest_framework import viewsets, permissions
from .models import Ticket
from .serializers import TicketSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.role == 'client':
            return self.queryset.filter(created_by=user)
        elif user.role == 'agent':
            return self.queryset.all()
        return self.queryset.none()
