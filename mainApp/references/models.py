from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    customer_code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name} ({self.customer_code})"


class Survey(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)  

    def __str__(self):
        return f"Survey by {self.customer.name}"
