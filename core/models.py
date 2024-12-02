from django.db import models


# Alumni database model
class AlumniModel(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100)
    email = models.EmailField()
    graduation_year = models.IntegerField()
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    linkedin = models.URLField()
    image = models.ImageField(upload_to='alumni/', default='alumni/default.png', blank=True, null=True)

    def __str__(self):
        return self.full_name

# Student database model
class StudentModel(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to='student/', default='student/default.png', blank=True, null=True)

    def __str__(self):
        return self.full_name
    
class Both(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email
