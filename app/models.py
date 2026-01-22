from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Category(models.Model):
    type = models.CharField(max_length=255, choices=[("Fintness", "Fitness"), ("Weights", "Weights")])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.type
    
    class Meta:
        ordering= ['created_at']
        verbose_name_plural = "Categories"

##############################################################################################################

class Tag(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
    

##############################################################################################################

class Record(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=11, blank=True, null=True, unique=True, validators=[RegexValidator(regex=r"^\d{11}$", message="Phone number must be 11 digits")]) # (unique) constraint already create index on that field, so there is no need for "db_index" attr
    tall = models.DecimalField(max_digits=3, decimal_places=2)
    weight = models.PositiveIntegerField()
    address = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="records")
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Heroes"
        indexes = [
            models.Index(fields=['first_name'], name="idx_first_name"),
            models.Index(fields=['last_name'], name="idx_last_name"),
        ]
        
        
# (Notes)

# There are two level of index creation on a model fields (db_index=True vs Meta.indexes):

# 1- Field-Level: first_name = models.CharField(max_length=255, db_index=True)

# 2- Meta-Level: indexes = [models.Index(fields=["first_name"])] 

# Both create indexes
# ✅ Best practice: use Meta.indexes for clarity and control

# Naming indexes (recommended)
# models.Index(fields=["first_name"], name="idx_record_first_name")
# Helps in:  DB (Debugging / Migrations/ Performance tuning)
