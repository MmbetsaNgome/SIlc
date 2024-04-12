import django
from django.shortcuts import render
from datetime import datetime
from django.db.models import Sum 
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from django.http import Http404
from rest_framework.response import Response
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from silc.models import *


from silc.serializers import UserSerializer,SilcGroupSerializer,MemberSerializer,RoleSerializer,GroupRoleSerializer,SavingSerializer,LoanSerializer,SocialFundSerializer,FineSerializer, CycleSerializer, GuarantorSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class SilcGroupViewSet(viewsets.ModelViewSet):
    queryset = SILCGroup.objects.all()
    serializer_class = SilcGroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'])  
    def total_contributions(self, request, pk=None):
        member = get_object_or_404(Member, pk=pk)
        total_savings = member.savings.aggregate(Sum('amount'))['amount__sum'] or 0
        total_social_fund = member.social_funds.aggregate(Sum('contribution_amount'))['contribution_amount__sum'] or 0

        total_contributions = total_savings + total_social_fund
        return Response({'total_contributions': total_contributions})

    @action(detail=True, methods=['get'])
    def outstanding_loans(self, request, pk=None):
        member = get_object_or_404(Member, pk=pk)
        loans = member.loans.filter(status="Pending")
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data)

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupRoleViewSet(viewsets.ModelViewSet):
    queryset = GroupRole.objects.all()
    serializer_class = GroupRoleSerializer
    permission_classes = [permissions.IsAuthenticated]

class SavingViewSet(viewsets.ModelViewSet):
    queryset = Saving.objects.all()
    serializer_class = SavingSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get']) 
    def savings_per_year(self, request):
        year = request.query_params.get('year')
        if not year:
            return Response({'error': 'year parameter is required'}, status=400)

        start_date = datetime(int(year), 1, 1)
        end_date = datetime(int(year), 12, 31)

        savings_data = Saving.objects.filter(
            date_contributed__gte=start_date,
            date_contributed__lte=end_date
        ).aggregate(Sum('amount'))

        return Response(savings_data)

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [permissions.IsAuthenticated]

class SocialFundViewSet(viewsets.ModelViewSet):
    queryset = SocialFund.objects.all()
    serializer_class = SocialFundSerializer
    permission_classes = [permissions.IsAuthenticated]

class FineViewSet(viewsets.ModelViewSet):
    queryset = Fine.objects.all()
    serializer_class = FineSerializer
    permission_classes = [permissions.IsAuthenticated]

class CycleViewSet(viewsets.ModelViewSet):
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer
    permission_classes = [permissions.IsAuthenticated]

class GuarantorViewSet(viewsets.ModelViewSet):
    queryset = Guarantor.objects.all()
    serializer_class = GuarantorSerializer
    permission_classes = [permissions.IsAuthenticated]