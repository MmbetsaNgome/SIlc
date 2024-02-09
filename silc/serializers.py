from django.contrib.auth.models import Group, User
from rest_framework import serializers
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
    class Meta:
        model = Member
        fields = ['id','group','name', 'id_number', 'phone_number', 'email', 'role', 'date_of_joining', 'status','gender']

class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ['name', 'permissions']

class GroupRoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroupRole
        fields = ['group','user', 'role']

class SavingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Saving
        fields = ['member', 'amount', 'date_contributed','notes']

class LoanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Loan
        fields = ['member','amount', 'interest_rate', 'date_issued', 'repayment_due_date','status']

class SocialFundSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SocialFund
        fields = ['member','contribution_amount', 'date_contributed','purpose']

class FineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fine
        fields = ['amount', 'reason', 'date_issued','status']

class CycleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cycle
        fields = ['start_date', 'end_date','active']

class GuarantorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guarantor
        fields = ['id_number', 'name', 'email', 'loan','relationship_with_loanee']