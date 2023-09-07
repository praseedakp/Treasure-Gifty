from django import forms

# customer form:
class customerform(forms.Form):
    fname=forms.CharField(max_length=50)
    lname=forms.CharField(max_length=50)
    state=forms.CharField(max_length=50)
    image=forms.FileField()
    uname=forms.CharField(max_length=50)
    passw=forms.CharField(max_length=50)
    confpass=forms.CharField(max_length=50)
    email=forms.EmailField()
    phone=forms.IntegerField()

# login details:
class costomerlogin(forms.Form):
    uname=forms.CharField(max_length=50)
    passw=forms.CharField(max_length=50)

# forms of admin page:
class adminform(forms.Form):
    adminusername=forms.CharField(max_length=50)
    adminpassw=forms.CharField(max_length=50)

# product forms
class productform(forms.Form):
    productname=forms.CharField(max_length=50)
    proid=forms.CharField(max_length=20)
    prodes=forms.CharField(max_length=550)
    proimage=forms.FileField()
    proprice=forms.IntegerField()


# wishform:
class wishform(forms.Form):
    uid=forms.IntegerField()
    pid=forms.IntegerField()
    pname=forms.CharField(max_length=50)
    pcid=forms.CharField(max_length=50)
    prode=forms.CharField(max_length=500)
    pimage=forms.FileField()
    price=forms.IntegerField()


#cart forms:
class cartform(forms.Form):
    carid=forms.IntegerField()
    cid=forms.IntegerField()
    cname=forms.CharField(max_length=50)
    cdid=forms.CharField(max_length=50)
    cimage=forms.FileField()
    cprice=forms.IntegerField()

##forms:video forms:
class videoform(forms.Form):
    vname=forms.CharField(max_length=30)
    video=forms.FileField()
    pdfname=forms.CharField(max_length=30)
    pdf=forms.FileField()




# second date auto:
class prdgalleryforms(forms.Form):
    pdtfname=forms.CharField(max_length=20)
    pdtfimage=forms.FileField()
    pdtfquan=forms.IntegerField()
    pdtffea=forms.CharField(max_length=200)
    pdtfdate=forms.DateField()
    pdtfnewname=forms.CharField(max_length=20)
    pdtfnewimage=forms.FileField()
    pdtfnewquan=forms.IntegerField()
    pdtffeanew=forms.CharField(max_length=200)
    pdtfdatenew=forms.DateField()

#newsfeed forms:
class newsfeedform(forms.Form):
    heading=forms.CharField(max_length=100)
    content=forms.CharField(max_length=400)
    image=forms.FileField()
    rate=forms.IntegerField()
    discount=forms.IntegerField()
    date=forms.DateField()

# payment forms:
class paymentform(forms.Form):
    fname=forms.CharField(max_length=50)
    email=forms.EmailField()
    phone=forms.IntegerField()
    gender=forms.CharField(max_length=10)
    location=forms.CharField(max_length=50)
    date=forms.DateField()
    select=forms.CharField(max_length=50)
    address=forms.CharField(max_length=250)

#recomented product forms:
class recommentedforms(forms.Form):
    pdtreconame=forms.CharField(max_length=50)
    pdtrecoimage=forms.FileField()


#review of customer:
class reviewforms(forms.Form):
    cusimage=forms.FileField()
    cuname=forms.CharField(max_length=50)
    comments=forms.CharField(max_length=500)
    deleplace=forms.CharField(max_length=100)
    deldate=forms.DateField()
    occation=forms.CharField(max_length=60)

