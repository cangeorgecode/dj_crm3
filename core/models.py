from django.db import models

CHOICES = (
    ('prospect', 'prospect'),
    ('lead', 'lead'),
    ('customer', 'customer'),
)

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=50)
    biz_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=CHOICES, default="prospect")
    todos = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return(f"{self.full_name}")


