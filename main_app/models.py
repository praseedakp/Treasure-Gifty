from django.db import models

# Create your models here.

# customer registration
class customerregmodel(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    image=models.FileField(upload_to='main_app/static')
    uname=models.CharField(max_length=50)
    passw=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    def __str__(self):
        return self.fname


# model for products
class productmodel(models.Model):
    productname=models.CharField(max_length=50)
    proid=models.CharField(max_length=20)
    prodes=models.CharField(max_length=550)
    proimage=models.FileField(upload_to='main_app/static')
    proprice=models.IntegerField()
    def __str__(self):
        return self.productname


# wishlist model:favourite one
class wishmodel(models.Model):
    uid=models.IntegerField()
    pid=models.IntegerField()
    pname=models.CharField(max_length=50)
    pcid=models.CharField(max_length=50)
    prode=models.CharField(max_length=500)
    pimage=models.FileField()
    price=models.IntegerField()
    def __str__(self):
        return self.pname

# cart model:payment page
class cartmodel(models.Model):
    carid=models.IntegerField()
    cid=models.IntegerField()
    cname=models.CharField(max_length=50)
    cdid=models.CharField(max_length=50)
    cimage=models.FileField()
    cprice=models.IntegerField()
    def __str__(self):
        return self.cdid

# model for video upload
class videomodel(models.Model):
    vname=models.CharField(max_length=50)
    video=models.FileField(upload_to='main_app/static')
    pdfname=models.CharField(max_length=50)
    pdf=models.FileField(upload_to='main_app/static')
    def __str__(self):
        return self.vname



# model for gallery product
class prdgallerymodel(models.Model):
    pdtfname=models.CharField(max_length=20)
    pdtfimage=models.FileField(upload_to='main_app/static')
    pdtfquan=models.IntegerField()
    pdtffea=models.CharField(max_length=200)
    pdtfdate=models.DateField()
    pdtfnewname=models.CharField(max_length=20)
    pdtfnewimage=models.FileField(upload_to='main_app/static')
    pdtfnewquan=models.IntegerField()
    pdtffeanew=models.CharField(max_length=200)
    pdtfdatenew=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.pdtfname

#newsfeed model:
class newsfeedmodel(models.Model):
    heading=models.CharField(max_length=100)
    content=models.CharField(max_length=400)
    image=models.FileField(upload_to='main_app/static')
    rate=models.IntegerField()
    discount=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.heading


#model for news selection:wishlist
class newswishmodel(models.Model):
    newsurid=models.IntegerField()
    newsid=models.IntegerField()
    wnhead=models.CharField(max_length=100)
    wncon=models.CharField(max_length=400)
    wnimage=models.FileField()
    wnrate=models.IntegerField()
    wndiscount=models.IntegerField()
    date=models.DateField()
    def __str__(self):
        return self.newsurid



# payment model:
class paymentmodel(models.Model):
    choice=[('Creditcard','Creditcard'),
            ('Debitcard','Debitcard'),
            ('Paytym','Paytym'),
            ('Googlepay','Googlepay')
            ]
    fname=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    gender=models.CharField(max_length=10)
    location=models.CharField(max_length=50)
    date=models.DateField()
    select=models.CharField(max_length=50,choices=choice)
    address=models.CharField(max_length=250)
    def __str__(self):
        return self.fname

##recomentation system:
class recommendedmodel(models.Model):
    pdtreconame=models.CharField(max_length=50)
    pdtrecoimage=models.FileField(upload_to='main_app/static')
    def __str__(self):
        return self.pdtreconame

# review of customer:
class reviewmodel(models.Model):
    cusimage=models.FileField(upload_to='main_app/static')
    cuname=models.CharField(max_length=50)
    comments=models.CharField(max_length=500)
    deleplace=models.CharField(max_length=100)
    deldate=models.DateField()
    occation=models.CharField(max_length=60)
    def __str__(self):
        return self.cuname


