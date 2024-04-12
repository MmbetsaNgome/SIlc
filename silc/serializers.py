from django.contrib.auth.models import Group, User
from rest_framework import serializers
from django.db.models import Sum
from silc.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class SilcGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SILCGroup
        fields = ['id','name', 'location','date_started', 'email', 'contact_number']

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    # group = SilcGroupSerializer(read_only=True)
    group = serializers.SlugRelatedField(slug_field='name',queryset=SILCGroup.objects.all())
    current_balance = serializers.SerializerMethodField()
    total_contributions = serializers.SerializerMethodField()

    def get_current_balance(self, obj):
        total_savings = obj.savings.aggregate(Sum('amount'))['amount__sum'] or 0
        total_loans = obj.loans.filter(status='Pending').aggregate(Sum('amount'))['amount__sum'] or 0
        return total_savings - total_loans

    def get_total_contributions(self, obj):
        total_savings = obj.savings.aggregate(Sum('amount'))['amount__sum'] or 0
        total_social_fund = obj.social_funds.aggregate(Sum('contribution_amount'))['contribution_amount__sum'] or 0
        return total_savings + total_social_fund

    class Meta:
        model = Member
        fields = ['id', 'group', 'name', 'id_number', 'phone_number', 'email', 'role', 'date_of_joining', 'status', 'gender', 'current_balance', 'total_contributions']
class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ['name', 'permissions']

class GroupRoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroupRole
        fields = ['group','user', 'role']

class SavingSerializer(serializers.HyperlinkedModelSerializer):
    member = serializers.SlugRelatedField(slug_field='name',queryset=Member.objects.all())
    class Meta:
        model = Saving
        fields = ['member', 'amount', 'date_contributed','notes']

class LoanSerializer(serializers.HyperlinkedModelSerializer):
    member = serializers.SlugRelatedField(slug_field='name',queryset=Member.objects.all())
    class Meta:
        model = Loan
        fields = ['member','amount', 'interest_rate', 'date_issued', 'repayment_due_date','status']

class SocialFundSerializer(serializers.HyperlinkedModelSerializer):
    member = serializers.SlugRelatedField(slug_field='name',queryset=Member.objects.all())
    class Meta:
        model = SocialFund
        fields = ['member','contribution_amount', 'date_contributed','purpose']

class FineSerializer(serializers.HyperlinkedModelSerializer):
    member = serializers.SlugRelatedField(slug_field='name',queryset=Member.objects.all())
    class Meta:
        model = Fine
        fields = ['member','amount', 'reason', 'date_issued','status']

class CycleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cycle
        fields = ['start_date', 'end_date','active']

class GuarantorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guarantor
        fields = ['id_number', 'name', 'email', 'loan','relationship_with_loanee']