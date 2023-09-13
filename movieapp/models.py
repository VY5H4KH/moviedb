from django.db import models

class Movie(models.Model):
    mov_id = models.AutoField(primary_key=True)
    mov_name = models.CharField(max_length=120)
    mov_date = models.CharField(max_length=10)
    mov_rat = models.DecimalField(max_digits=2,decimal_places=1)
    mov_desc = models.TextField()
    mov_dir = models.CharField(max_length=200)
    mov_act = models.CharField(max_length=200)
    mov_wir = models.CharField(max_length=200)
    mov_tra = models.URLField()
    mov_wat = models.URLField()
    mov_img = models.ImageField(upload_to='')
    mov_pro = models.ImageField(upload_to='',null=True,blank=True)

    def __str__(self):
        return self.mov_name

class Review(models.Model):
    Name = models.CharField(max_length=100)
    Mail_id =  models.EmailField(max_length=100)
    Your_Review = models.TextField()
    movi_name = models.ForeignKey('Movie',on_delete=models.CASCADE)

    def __str__(self):
        return self.Name