from django.db import models

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    about = models.TextField()

    type = models.CharField(
        max_length=100,
        choices=(
            ('IT', 'IT'),
            ('Non IT', 'Non IT'),
            ('mobile phone', 'mobile phone')
        )
    )

    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


# Employee model 
    def __str__(self):
        return f"{self.name} -- {self.location}"

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=50 , choices=( 
        
        ('Manager', 'Manager'),
        ('Developer', 'Developer'),
        ('Tester', 'Tester'),
        ('Designer', 'Designer')
    ))
  

    Company= models.ForeignKey(Company, on_delete=models.CASCADE)