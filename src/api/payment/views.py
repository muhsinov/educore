from rest_framework import viewsets
from payment.models import Payment
from .serializers import PaymentSerializer
from ..permissions import IsAdminOrStudentReadOnly

class PaymentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAdminOrStudentReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Payment.objects.all()
        elif hasattr(user, 'student'):
            return Payment.objects.filter(student_group__student=user.student)
        return Payment.objects.none()