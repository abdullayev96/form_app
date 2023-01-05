from django.db import models



class Customer(models.Model):
    first_name=models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=False, null=False)
    place = models.IntegerField(blank=False, null=False, choices=[(1, "Toshkent"), (2, "Andijon"), (3, "Farg'ona"), (4, "Namangan"),
                                                                  (5, "Sirdaryo"), (6, "Jizzax"),  (7, "Samarqand"),  (8, "Navoiy"),
                                                                  (9, "Surxondaryo"), (10, "Qashqadaryo"), (11, "Xorazm"), (12, "Qoraqalpoq"),], default=1)
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    message = models.TextField(blank=False, null=False)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
