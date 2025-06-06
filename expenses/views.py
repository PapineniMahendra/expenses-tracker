from rest_framework import generics, permissions
from .models import Expense
from .serializers import ExpenseSerializer
from rest_framework.response import Response
from django.db.models import Sum
from rest_framework.views import APIView
from datetime import datetime
from django.db.models.functions import TruncDay, TruncMonth, TruncWeek

class ExpenseListCreateView(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Expense.objects.filter(user=user)
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ExpenseAnalyticsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        expenses = Expense.objects.filter(user=user)

        total = expenses.aggregate(total=Sum('amount'))['total'] or 0

        category_data = expenses.values('category').annotate(total=Sum('amount'))

        daily = expenses.annotate(date_group=TruncDay('date')).values('date_group').annotate(total=Sum('amount'))
        weekly = expenses.annotate(week_group=TruncWeek('date')).values('week_group').annotate(total=Sum('amount'))
        monthly = expenses.annotate(month_group=TruncMonth('date')).values('month_group').annotate(total=Sum('amount'))

        return Response({
            "total_expenses": total,
            "category_breakdown": category_data,
            "daily": daily,
            "weekly": weekly,
            "monthly": monthly,
        })
