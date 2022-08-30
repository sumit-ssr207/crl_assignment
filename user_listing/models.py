from django.db import models

# Create your models here.
class m_usernames(models.Model):
    username = models.CharField(max_length=100,primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10,null=True)
    id_type = models.CharField(max_length=100,null=True)
    id_value = models.CharField(max_length=150,null=True)


class m_userdetails(models.Model):
    username = models.ForeignKey(m_usernames, on_delete=models.CASCADE)
    email = models.CharField(max_length=100,null=True)
    location_city = models.CharField(max_length=100,null=True)
    location_state = models.CharField(max_length=100,null=True)
    loation_country = models.CharField(max_length=100,null=True)
    location_postcode = models.CharField(max_length=100,null=True)
    dob = models.CharField(max_length=100,null=True)
    registered_date = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=100,null=True)
    cell = models.CharField(max_length=100,null=True)
    picture = models.CharField(max_length=200,null=True)
    nat = models.CharField(max_length=100,null=True)

