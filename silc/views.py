from django.shortcuts import render
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