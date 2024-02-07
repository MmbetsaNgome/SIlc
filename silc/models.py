from django.db import models
from django.utils import timezone  # Corrected import
from django.contrib.auth.models import User

# Create your models here.
class SILCGroup(models.Model):
    name = models.CharField(max_length=200, help_text='The name of the SILC group.')
    location = models.CharField(max_length=300, help_text='The physical location where the group meets.')
    date_started = models.DateField(help_text='The date when the group began operation.')
    email = models.EmailField(help_text='Contact email for the group.')
    contact_number = models.CharField(max_length=15, help_text='Contact phone number for the group.')

    def __str__(self):
        return f"{self.name} located at {self.location} started on {self.date_started}"


# Member model as just defined
class Member(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    STATUS_CHOICES = [
        ('A', 'Active'),
        ('D', 'Dormant'),
    ]

    group = models.ForeignKey(SILCGroup, on_delete=models.CASCADE, related_name='members')
    name = models.CharField(max_length=200, help_text='Full name of the member.')
    id_number = models.CharField(max_length=100, unique=True, help_text='ID number of the member.')
    phone_number = models.CharField(max_length=15, help_text='Phone number of the member.')
    email = models.EmailField(help_text='Email address of the member.')
    role = models.CharField(max_length=100, help_text='Role of the member in the group.')
    date_of_joining = models.DateField(default=timezone.now, help_text='The date when the member joined the group.')  # Corrected
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A', help_text='Whether the member is active or dormant.')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, help_text='Gender of the member.')

    def __str__(self):
        return f"{self.name} ({self.role}) - {self.group.name}"

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'
class Role(models.Model):
    name = models.CharField(max_length=100)
    permissions = models.TextField(help_text='Custom permissions or rights, as a JSON string or similar')

    def __str__(self):
        return self.name

class GroupRole(models.Model):
    group = models.ForeignKey(SILCGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} as {self.role.name} in {self.group.name}"


class Saving(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='savings')
    amount = models.DecimalField(max_digits=10, decimal_places=2, help_text='Amount saved by the member.')
    date_contributed = models.DateField(default=timezone.now, help_text='Date when the contribution was made.')
    notes = models.TextField(blank=True, null=True, help_text='Any additional notes about the saving contribution.')

    def __str__(self):
        return f"{self.member.name} - {self.amount} on {self.date_contributed}"

    class Meta:
        verbose_name = 'Saving'
        verbose_name_plural = 'Savings'

class Loan(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='loans')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    date_issued = models.DateField(default=timezone.now)
    repayment_due_date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Pending', 'Pending'), ('Paid', 'Paid'), ('Overdue', 'Overdue')])

class SocialFund(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='social_funds')
    contribution_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_contributed = models.DateField(default=timezone.now)
    purpose = models.TextField(blank=True, null=True)

class Fine(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='fines')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.TextField()
    date_issued = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, choices=[('Paid', 'Paid'), ('Pending', 'Pending')])

class Cycle(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True, help_text="Is the cycle currently active?")

    def __str__(self):
        return f"Cycle starting {self.start_date} and ending {self.end_date}"


class Guarantor(models.Model):
    id_number = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    loan = models.ForeignKey('Loan', on_delete=models.CASCADE, related_name='guarantors')
    relationship_with_loanee = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.relationship_with_loanee}) for Loan ID {self.loan.id}"
