
from django.db import models

# User-level
# class User(AbstractUser):
#     def __str__(self):
#         return self.username

# class Friendship(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')
#     friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_of')

    # class Meta:
    #     unique_together = ('user', 'friend')

    # def __str__(self):
    #     return f"{self.user.username} is friends with {self.friend.username}"

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    account_id = models.CharField(max_length=255)
    cluster_name_adjusted = models.CharField(max_length=255)
    currency_code = models.CharField(max_length=10)
    merchant_category = models.CharField(max_length=255)
    date_booked = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.amount} {self.currency_code}"

