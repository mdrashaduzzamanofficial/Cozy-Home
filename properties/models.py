from django.db import models
from users.models import CustomUser
from django.core.validators import MinValueValidator

class Property(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='properties')
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    bedrooms = models.IntegerField(validators=[MinValueValidator(0)])
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='properties/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Application(models.Model):
    tenant = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='applications')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='applications')
    status = models.CharField(max_length=20, choices=(
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ), default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tenant.username} - {self.property.title}"

class Lease(models.Model):
    tenant = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='leases')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='leases')
    start_date = models.DateField()
    end_date = models.DateField()
    file = models.FileField(upload_to='leases/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Lease for {self.property.title}"

class Payment(models.Model):
    tenant = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='payments')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=(
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ), default='pending')
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of {self.amount} for {self.property.title}"

class UserPreference(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='preference')
    max_budget = models.DecimalField(max_digits=10, decimal_places=2, default=1000)
    min_bedrooms = models.IntegerField(default=1)
    preferred_location = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Preferences for {self.user.username}"