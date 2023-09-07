from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
import os
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.contrib.auth import logout
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'index.html')

# customerregistration here
def regpage(request):
    if request.method=='POST':
        a=customerform(request.POST,request.FILES)
        if a.is_valid():
            fn=a.cleaned_data['fname']
            ln=a.cleaned_data['lname']
            st=a.cleaned_data['state']
            im=a.cleaned_data['image']
            un=a.cleaned_data['uname']
            ps=a.cleaned_data['passw']
            cp=a.cleaned_data['confpass']
            em=a.cleaned_data['email']
            ph=a.cleaned_data['phone']
            if ps==cp:
                b=customerregmodel(fname=fn,lname=ln,state=st,image=im,uname=un,passw=ps,email=em,phone=ph)
                b.save()
                subject="Congratulations...your Treasure Gifty(TG) account has been created"
                message=f"your username is {un}"
                email_from="ctpraseeda8064@gmail.com"
                email_to=em
                send_mail(subject,message,email_from,[email_to])
                return redirect(customerloginview)
            else:
                messages.warning(request,"Registration Failed!")
    return render(request,'customerregistration.html')


# login:for customer only with username and password case:
def customerloginview(request):
    if request.method=='POST':
        s=costomerlogin(request.POST)
        if s.is_valid():
            us=s.cleaned_data['uname']
            ps=s.cleaned_data['passw']
            r=customerregmodel.objects.all()
            for i in r:
                if i.uname==us and i.passw==ps:
                    request.session['id']=i.id
                    return redirect(customerpro)
            else:
                messages.warning(request,"Login Failed!")

                #return HttpResponse("login failed...")
    return render(request,'customerlogin.html')



# profile page for customers:
def customerpro(request):
    try:
        id1=request.session['id']
        a=customerregmodel.objects.get(id=id1)
        img=str(a.image).split('/')[-1]
        return render(request,'customerprofile.html',{'a':a,'img':img})
    except:
        return redirect(customerloginview)


#profilepage for customer edit:
def customeredit(request,id):
    a=customerregmodel.objects.get(id=id)
    img=str(a.image).split('/')[-1]
    if request.method=='POST':
        a.fname=request.POST.get('finame')
        a.lname=request.POST.get('laname')
        a.state=request.POST.get('state')
        a.uname=request.POST.get('uname')
        a.email=request.POST.get('email')
        a.phone=request.POST.get('phone')
        if len(request.FILES)!=0:
            if len(a.image)>0:
                os.remove(a.image.path)
            a.image=request.FILES['image']
        a.save()
        return redirect(customerpro)
    return render(request,'customeredit.html',{'a':a,'img':img})


# logout:profilepage
def logoutview(request):
    logout(request)
    return redirect(customerloginview)


#shows all details of the customers:adminpage
def fullcustomerde(request):
    b=customerregmodel.objects.all()
    id1=[]
    fn=[]
    ln=[]
    st=[]
    im=[]
    un=[]
    ps=[]
    em=[]
    ph=[]
    for i in b:
        id2=i.id
        id1.append(id2)
        f=i.fname
        fn.append(f)
        l=i.lname
        ln.append(l)
        s=i.state
        st.append(s)
        ima=str(i.image).split('/')[-1]
        im.append(ima)
        u=i.uname
        un.append(u)
        p=i.passw
        ps.append(p)
        e=i.email
        em.append(e)
        pho=i.phone
        ph.append(pho)
    pair=zip(id1,fn,ln,st,im,un,ps,em,ph)
    return render(request,'fullcustomerdisplay.html',{'b':pair})


#adminlogin
def adminlogin(request):
    if request.method=='POST':
        a=adminform(request.POST)
        if a.is_valid():
            username=a.cleaned_data['adminusername']
            password=a.cleaned_data['adminpassw']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                return redirect(adminpropage)
            else:
                return HttpResponse("Login failed")
    return render(request,'adminloginpage.html')

# admin profile page:
def adminpropage(request):
    return render(request,'adminprofilepage.html')


# product registration:admin
def productview(request):
    if request.method=='POST':
        a=productform(request.POST,request.FILES)
        if a.is_valid():
            pn=a.cleaned_data['productname']
            pid=a.cleaned_data['proid']
            des=a.cleaned_data['prodes']
            im=a.cleaned_data['proimage']
            pr=a.cleaned_data['proprice']
            b=productmodel(productname=pn,proid=pid,prodes=des,proimage=im,proprice=pr)
            b.save()
            return redirect(adminprodisplay)
        else:
            return HttpResponse("failed.... sorry... try again")

    return render(request,'productuploadpage.html')


# product display:for customer
def customerprodisplay(request):
    a=productmodel.objects.all()
    id1=[]
    prn=[]
    prid=[]
    prim=[]
    prd=[]
    prp=[]
    for i in a:
        id2=i.id
        id1.append(id2)
        p=i.productname
        prn.append(p)
        q=i.proid
        prid.append(q)
        im=str(i.proimage).split('/')[-1]
        prim.append(im)
        pd=i.prodes
        prd.append(pd)
        cp=i.proprice
        prp.append(cp)
    ppair=zip(id1,prn,prid,prim,prd,prp)
    return render(request,'customerproductdisplay.html',{'ppair':ppair})

# product display for admin with edit and delete button:
def adminprodisplay(request):
    a=productmodel.objects.all()
    id1=[]
    prn=[]
    prid=[]
    prim=[]
    prd=[]
    prp=[]
    for i in a:
        id2=i.id
        id1.append(id2)
        p=i.productname
        prn.append(p)
        q=i.proid
        prid.append(q)
        im=str(i.proimage).split('/')[-1]
        prim.append(im)
        pd=i.prodes
        prd.append(pd)
        cp=i.proprice
        prp.append(cp)
    ppair=zip(id1,prn,prid,prim,prd,prp)
    return render(request,'adminproductdisplay.html',{'ppair':ppair})


#delete code for uploaded product:admin
def adminprodelete(request,id):
    a=productmodel.objects.get(id=id)
    os.remove(str(a.proimage))
    a.delete()
    return redirect(adminprodisplay)

# editcode for admin productpage
def adminproedit(request,id):
    a=productmodel.objects.get(id=id)
    img=str(a.proimage).split('/')[-1]
    if request.method=='POST':
        a.productname=request.POST.get('proname')
        a.proid=request.POST.get('proid')
        a.prodes=request.POST.get('prodes')
        a.proprice=request.POST.get('proprice')
        if len(request.FILES)!=0:
            if len(a.proimage)>0:
                os.remove(a.proimage.path)
            a.proimage=request.FILES['proimage']
        a.save()
        return redirect(adminprodisplay)
    return render(request,'adminproductedit.html',{'a':a,'img':img})

# add to wishlist:by customers
def wishlistview(request,id):
    a=productmodel.objects.get(id=id)
    ig=str(a.proimage).split('/')[-1]
    wish=wishmodel.objects.all()
    for i in wish:
        if i.pid==a.id and i.uid==request.session['id']:
            return redirect(recowishdisplay)
    b=wishmodel(pname=a.productname,pcid=a.proid,prode=a.prodes,pimage=ig,price=a.proprice,pid=a.id,uid=request.session['id'])
    b.save()
    return redirect(viewwishlist)


# wishlistdisplay:for customers
def viewwishlist(request):
    id=request.session['id']
    b=wishmodel.objects.all()
    u=[]
    pn=[]
    pc=[]
    pd=[]
    pi=[]
    pr=[]
    for i in b:
        s=i.uid
        u.append(s)
        k=i.pname
        pn.append(k)
        l=i.pcid
        pc.append(l)
        o=i.prode
        pd.append(o)
        m=str(i.pimage).split('/')[-1]
        pi.append(m)
        n=i.price
        pr.append(n)
    pt=zip(u,pn,pc,pd,pi,pr)
    return render(request,'wishlistdisplay.html',{'pt':pt,'id':id})


#single display the card for customers
def singledisplay(request,id):
    a=productmodel.objects.get(id=id)
    im=str(a.proimage).split('/')[-1]
    return render(request,'singleviewcard.html',{'a':a,'im':im})


#remove from wishlist
def wishremoveone(request,id):
    k=customerregmodel.objects.get(id=id)
    l=productmodel.objects.all()
    b=wishmodel.objects.all()
    for i in b:
        for j in l:
            if j.proid==i.pcid:
                if k.id==i.uid:
                    i.delete()
                    return redirect(viewwishlist)

#add to cart:customers
#add to cart from product display
def addtocart(request,id):
    a=productmodel.objects.get(id=id)
    im=str(a.proimage).split('/')[-1]
    cart=cartmodel.objects.all()
    for i in cart:
        if i.carid==a.id and i.cid==request.session['id']:
            return redirect(recommenteddisplay)
    b=cartmodel(cname=a.productname,cdid=a.proid,cimage=im,cprice=a.proprice,carid=a.id,cid=request.session['id'])
    b.save()
    return redirect(newpagecartdesign)


# new cart design page:
def newpagecartdesign(request):
    id=request.session['id']
    b=cartmodel.objects.all()
    u=[]
    p=[]
    pd=[]
    pi=[]
    pr=[]
    total=0
    sub=23.00
    for i in b:
        s=i.cid
        u.append(s)
        k=i.cname
        p.append(k)
        l=i.cdid
        pd.append(l)
        m=str(i.cimage).split('/')[-1]
        pi.append(m)
        n=i.cprice
        pr.append(n)
        g=i.cid
        if g==id:
            total+=i.cprice
    sub+=total
    pt=zip(u, p, pd, pi, pr)
    return render(request,'newcartdesignpage.html',{'pt':pt,'total':total,'id':id,'sub':sub})

#delete from cart
def cardremoveone(request,id):
    k=customerregmodel.objects.get(id=id)
    l=productmodel.objects.all()
    h=cartmodel.objects.all()
    for i in h:
        for j in l:
            if j.id == i.cid:
                i.delete()
                return redirect(newpagecartdesign)


#video and broshures:upload by admin
def videoupload(request):
    if request.method=='POST':
        a=videoform(request.POST,request.FILES)
        if a.is_valid():
            vn=a.cleaned_data['vname']
            vd=a.cleaned_data['video']
            pd=a.cleaned_data['pdfname']
            pf=a.cleaned_data['pdf']
            b=videomodel(vname=vn,video=vd,pdfname=pd,pdf=pf)
            b.save()
            return redirect(adminvideodisplay)
        else:
            return HttpResponse("upload failed.... sorry... try again")
    return render(request,'videoupload.html')



###display of video and broshures for customers
def videodisp(request):
    a=videomodel.objects.all()
    vn=[]
    vd=[]
    pn=[]
    pdf=[]
    for i in a:
        k=i.vname
        vn.append(k)
        l=str(i.video).split('/')[-1]
        vd.append(l)
        m=i.pdfname
        pn.append(m)
        n=str(i.pdf).split('/')[-1]
        pdf.append(n)
    p=zip(vn,vd,pn,pdf)
    return render(request,'videocustomerdisplay.html',{'p':p})


#display video for admin
def adminvideodisplay(request):
    a=videomodel.objects.all()
    d=[]
    vn=[]
    vd=[]
    pn=[]
    pdf=[]
    for i in a:
        r=i.id
        d.append(r)
        k=i.vname
        vn.append(k)
        l=str(i.video).split('/')[-1]
        vd.append(l)
        m=i.pdfname
        pn.append(m)
        n=str(i.pdf).split('/')[-1]
        pdf.append(n)
    pv=zip(d,vn,vd,pn,pdf)
    return render(request,'videoadmindisplay.html',{'pv':pv})

#delete video and broshure from admin
def vidpdfdelete(request,id):
    f=videomodel.objects.get(id=id)
    os.remove(str(f.video))
    os.remove(str(f.pdf))
    f.delete()
    return redirect(adminvideodisplay)

#edit the video and broshure page for admin:
def videopdfedit(request,id):
    d=videomodel.objects.get(id=id)
    vid=str(d.video).split('/')[-1]
    pd=str(d.pdf).split('/')[-1]
    if request.method=='POST':
        d.vname=request.POST.get('videoeditna')
        d.pdfname=request.POST.get('pdfeditna')
        if request.FILES.get('video')==None:
            d.save()
        else:
            d.video=request.FILES['video']
        if request.FILES.get('pdf')==None:
            d.save()
        else:
            d.pdf=request.FILES['pdf']
        d.save()
        return redirect(adminvideodisplay)
    return render(request,'videopdfedit.html',{'d':d,'vid':vid,'pd':pd})



#product gallery admin upload:
def newgallerypro(request):
    if request.method=='POST':
        a=prdgalleryforms(request.POST,request.FILES)
        if a.is_valid():
            k=a.cleaned_data['pdtfname']
            l=a.cleaned_data['pdtfimage']
            m=a.cleaned_data['pdtfquan']
            n=a.cleaned_data['pdtffea']
            o=a.cleaned_data['pdtfdate']
            p=a.cleaned_data['pdtfnewname']
            q=a.cleaned_data['pdtfnewimage']
            r=a.cleaned_data['pdtfnewquan']
            s=a.cleaned_data['pdtffeanew']
            t=a.cleaned_data['pdtfdatenew']
            b=prdgallerymodel(pdtfname=k,pdtfimage=l,pdtfquan=m,pdtffea=n,pdtfdate=o,pdtfnewname=p,pdtfnewimage=q,pdtfnewquan=r,pdtffeanew=s,pdtfdatenew=t)
            b.save()
            return redirect(galleryproadminisplay)
        else:
            return HttpResponse("upload failed.... sorry... try again")
    return render(request,'galleryupload.html')


#all customer display product gallery with old and new products:
def prdgallerycustomerdisp(request):
    a=prdgallerymodel.objects.all()
    c=[]
    d=[]
    e=[]
    f=[]
    g=[]
    h=[]
    y=[]
    j=[]
    k=[]
    l=[]
    for i in a:
        m=i.pdtfname
        c.append(m)
        n=str(i.pdtfimage).split('/')[-1]
        d.append(n)
        o=i.pdtfquan
        e.append(o)
        p=i.pdtffea
        f.append(p)
        q=i.pdtfdate
        g.append(q)
        r=i.pdtfnewname
        h.append(r)
        s=str(i.pdtfnewimage).split('/')[-1]
        y.append(s)
        t=i.pdtfnewquan
        j.append(t)
        u=i.pdtffeanew
        k.append(u)
        v=i.pdtfdatenew
        l.append(v)
    pr=zip(c,d,e,f,g,h,y,j,k,l)
    return render(request,'newproductdisplay.html',{'pr':pr})


#display the product for admin with edit and delete:
def galleryproadminisplay(request):
    a=prdgallerymodel.objects.all()
    id1=[]
    c=[]
    d=[]
    e=[]
    f=[]
    g=[]
    h=[]
    y=[]
    j=[]
    k=[]
    l=[]
    for i in a:
        id2=i.id
        id1.append(id2)
        m=i.pdtfname
        c.append(m)
        n=str(i.pdtfimage).split('/')[-1]
        d.append(n)
        o=i.pdtfquan
        e.append(o)
        p=i.pdtffea
        f.append(p)
        q=i.pdtfdate
        g.append(q)
        r=i.pdtfnewname
        h.append(r)
        s=str(i.pdtfnewimage).split('/')[-1]
        y.append(s)
        t=i.pdtfnewquan
        j.append(t)
        u=i.pdtffeanew
        k.append(u)
        v=i.pdtfdatenew
        l.append(v)
    pa=zip(id1,c,d,e,f,g,h,y,j,k,l)
    return render(request,'pdtgalleryadmindisplay.html',{'pa':pa})



#delete data from pdtgallery:admin
def prdtgallerydelete(request,id):
    a=prdgallerymodel.objects.get(id=id)
    os.remove(str(a.pdtfimage))
    os.remove(str(a.pdtfnewimage))
    a.delete()
    return redirect(galleryproadminisplay)


#edit the pdtgallery:admin
def prdgalleryeditview(request,id):
    a=prdgallerymodel.objects.get(id=id)
    im=str(a.pdtfimage).split('/')[-1]
    img=str(a.pdtfnewimage).split('/')[-1]
    if request.method=='POST':
        a.pdtfname=request.POST.get('pdtfname')
        a.pdtfquan=request.POST.get('pdtfquan')
        a.pdtffea=request.POST.get('pdtffea')
        a.pdtfnewname=request.POST.get('pdtfnewname')
        a.pdtfnewquan=request.POST.get('pdtfnewquan')
        a.pdtffeanew=request.POST.get('pdtffeanew')
        if request.POST.get('pdtfdate')=='':
            a.save()
        else:
            a.pdtfdate=request.POST.get('pdtfdate')
        if request.POST.get('pdtfdatenew') == '':
            a.save()
        else:
            a.pdtfdatenew=request.POST.get('pdtfdatenew')
        a.save()
        if len(request.FILES)!=0:
            if len(a.pdtfimage)>0:
                os.remove(a.pdtfimage.path)
            a.pdtfimage=request.FILES['pdtfimage']
            if len(a.pdtfnewimage)>0:
                os.remove(a.pdtfnewimage.path)
            a.pdtfnewimage=request.FILES['pdtfnewimage']
        a.save()
        return redirect(galleryproadminisplay)
    return render(request,'editprdgallery.html',{'a':a,'im':im,'img':img})


######newsfeed upload admin
def newsfeedview(request):
    if request.method=='POST':
        a=newsfeedform(request.POST,request.FILES)
        if a.is_valid():
            h=a.cleaned_data['heading']
            co=a.cleaned_data['content']
            im=a.cleaned_data['image']
            ra=a.cleaned_data['rate']
            di=a.cleaned_data['discount']
            dat=a.cleaned_data['date']
            b=newsfeedmodel(heading=h,content=co,image=im,rate=ra,discount=di,date=dat)
            b.save()
            return redirect(newsadmindisplay)
        else:
            return HttpResponse("upload failed.... sorry... try again")
    return render(request,'newsfeedadminupload.html')

#display news feed for all customers:
def newsfeedcustomerdisp(request):
    a=newsfeedmodel.objects.all()
    id1=[]
    ne=[]
    co=[]
    ia=[]
    ra=[]
    di=[]
    da=[]
    for i in a:
        w=i.id
        id1.append(w)
        k=i.heading
        ne.append(k)
        u=i.content
        co.append(u)
        l=str(i.image).split('/')[-1]
        ia.append(l)
        m=i.rate
        ra.append(m)
        n=i.discount
        di.append(n)
        o=i.date
        da.append(o)
    nc=zip(id1,ne,co,ia,ra,di,da)
    return render(request,'newsfeedcustomerdisplay.html',{'nc':nc})


#News feed display page for admin with edit and delete:
def newsadmindisplay(request):
    a=newsfeedmodel.objects.all()
    id1=[]
    ne=[]
    co=[]
    img=[]
    ra=[]
    di=[]
    da=[]
    for i in a:
        id2=i.id
        id1.append(id2)
        k=i.heading
        ne.append(k)
        u=i.content
        co.append(u)
        l=str(i.image).split('/')[-1]
        img.append(l)
        m=i.rate
        ra.append(m)
        n=i.discount
        di.append(n)
        o=i.date
        da.append(o)
    na=zip(id1,ne,co,img,ra,di,da)
    return render(request,'newsadmindisplay.html',{'na':na})


#delete data newsfeed by admin
def newsfeeddelete(request,id):
    a=newsfeedmodel.objects.get(id=id)
    os.remove(str(a.image))
    a.delete()
    return redirect(newsadmindisplay)


#edit the newsfeed by admin:
def newsfeededit(request,id):
    a=newsfeedmodel.objects.get(id=id)
    img=str(a.image).split('/')[-1]
    if request.method=='POST':
        a.heading=request.POST.get('heading')
        a.content=request.POST.get('content')
        a.rate=request.POST.get('rate')
        a.discount=request.POST.get('discount')
        if request.POST.get('date')=='':
            a.save()
        else:
            a.date=request.POST.get('date')
        a.save()
        if len(request.FILES)!=0:
            if len(a.image)>0:
                os.remove(a.image.path)
            a.image=request.FILES['image']
        a.save()
        return redirect(newsadmindisplay)
    return render(request,'editadminnewsfeed.html',{'a':a,'img':img})


#newswishlist for customers:
def newswishlistview(request,id):
    a=newsfeedmodel.objects.get(id=id)
    k=str(a.image).split('/')[-1]
    newswish=newswishmodel.objects.all()
    for i in newswish:
        if i.newsid==a.id and i.newsurid==request.session['id']:
            return redirect(recowishdisplay)
    b=newswishmodel(wnhead=a.heading,wncon=a.content,wnimage=k,wnrate=a.rate,wndiscount=a.discount,date=a.date,newsid=a.id,newsurid=request.session['id'])
    b.save()
    return redirect(viewnewswishlist)

#newsfeed wishdisplay:for customers
def viewnewswishlist(request):
    b=newswishmodel.objects.all()
    id=request.session['id']
    g=[]
    s=[]
    t=[]
    u=[]
    v=[]
    w=[]
    x=[]
    y=[]
    for i in b:
        h=i.newsurid
        g.append(h)
        j=i.newsid
        s.append(j)
        k=i.wnhead
        t.append(k)
        l=i.wncon
        u.append(l)
        m=str(i.wnimage).split('/')[-1]
        v.append(m)
        n=i.wnrate
        w.append(n)
        o=i.wndiscount
        x.append(o)
        p=i.date
        y.append(p)
    pz=zip(g,s,t,u,v,w,x,y)
    return render(request,'newswishlistdisplay.html',{'pz':pz,'id':id})

#########delete of the newswishlist from customer
def wishremovenews(request,id):
    k=customerregmodel.objects.get(id=id)
    b=newswishmodel.objects.all()
    for i in b:
        if k.id==i.newsurid:
            i.delete()
            return redirect(viewnewswishlist)



# payment verification:upload for customers
def paymentviewone(request):
    if request.method=='POST':
        a=paymentform(request.POST)
        if a.is_valid():
            nm=a.cleaned_data['fname']
            em=a.cleaned_data['email']
            ph=a.cleaned_data['phone']
            ge=a.cleaned_data['gender']
            lo=a.cleaned_data['location']
            da=a.cleaned_data['date']
            se=a.cleaned_data['select']
            ad=a.cleaned_data['address']
            b=paymentmodel(fname=nm,email=em,phone=ph,gender=ge,location=lo,date=da,select=se,address=ad)
            b.save()
            return redirect(paymentdisplay)
        else:
            return HttpResponse("payment failed")
    return render(request,'paymentpage.html')


#display payment page and print it:
def paymentdisplay(request):
    id1=request.session['id']
    s=customerregmodel.objects.all()
    b=cartmodel.objects.all()
    u=[]
    pr=[]
    total=0
    sub=23.00
    for i in b:
        g=i.cid
        u.append(g)
        n=i.cprice
        pr.append(n)
        h=i.cid
        if h == id1:
            total+=i.cprice
    sub+=total
    k=zip(u,pr)
    return render(request,'paymentdisplay.html',{'k':k,'s':s,'id1':id1,'total':total,'sub':sub})

#fullpayment display for admin:
def fullpaydisplaynew(request):
    h=paymentmodel.objects.all()
    return render(request,'customerfullpaymentdisplay.html',{'h':h})



#recommented view:upload by admin
def recommentedview(request):
    if request.method=='POST':
        a=recommentedforms(request.POST,request.FILES)
        if a.is_valid():
            nm=a.cleaned_data['pdtreconame']
            em=a.cleaned_data['pdtrecoimage']
            b=recommendedmodel(pdtreconame=nm,pdtrecoimage=em)
            b.save()
            return redirect(recoadmindisplay)
        else:
            return HttpResponse("failed....")
    return render(request,'recommepdtupload.html')

#display the recommented product for customers only:
#item already in cart
def recommenteddisplay(request):
    s=recommendedmodel.objects.all()
    r=[]
    f=[]
    for i in s:
        g=i.pdtreconame
        r.append(g)
        h=str(i.pdtrecoimage).split('/')[-1]
        f.append(h)
    pr=zip(r,f)
    return render(request,'recocustomerdisplay.html',{'pr':pr})

##display the recommented product in wishlistdisplay:customers
def recowishdisplay(request):
    s=recommendedmodel.objects.all()
    k=[]
    l=[]
    for i in s:
        g=i.pdtreconame
        k.append(g)
        h=str(i.pdtrecoimage).split('/')[-1]
        l.append(h)
    pi=zip(k,l)
    return render(request,'recowishdisplay.html',{'pi':pi})

#admin edit and delete:
#display the recommented product for customer:
def recoadmindisplay(request):
    s=recommendedmodel.objects.all()
    id1=[]
    rd=[]
    fd=[]
    for i in s:
        id2=i.id
        id1.append(id2)
        g=i.pdtreconame
        rd.append(g)
        h=str(i.pdtrecoimage).split('/')[-1]
        fd.append(h)
    pa=zip(id1,rd,fd)
    return render(request,'recoadmindisplay.html',{'pa':pa})


#delete:recommented products by admin
def recoadmindelete(request,id):
    f=recommendedmodel.objects.get(id=id)
    os.remove(str(f.pdtrecoimage))
    f.delete()
    return redirect(recoadmindisplay)

#edit recommented productsby admin:
def recoadminedit(request,id):
    a=recommendedmodel.objects.get(id=id)
    img=str(a.pdtrecoimage).split('/')[-1]
    if request.method=='POST':
        a.pdtreconame=request.POST.get('pdtreconame')
        if len(request.FILES)!=0:
            if len(a.pdtrecoimage)>0:
                os.remove(a.pdtrecoimage.path)
            a.pdtrecoimage=request.FILES['pdtrecoimage']
        a.save()
        return redirect(recoadmindisplay)
    return render(request,'recoadminedit.html',{'a':a,'img':img})


###customer review
def customerreview(request):
    if request.method=='POST':
        a=reviewforms(request.POST,request.FILES)
        if a.is_valid():
            nm=a.cleaned_data['cusimage']
            em=a.cleaned_data['cuname']
            ph=a.cleaned_data['comments']
            ge=a.cleaned_data['deleplace']
            lo=a.cleaned_data['deldate']
            da=a.cleaned_data['occation']
            b=reviewmodel(cusimage=nm,cuname=em,comments=ph,deleplace=ge,deldate=lo,occation=da)
            b.save()
            return redirect(reviewdisplayview)
        else:
            return HttpResponse("comments upload failed")
    return render(request,'pdtcustomerreview.html')

##display:review for customer in homepage
def reviewdisplayview(request):
    a=reviewmodel.objects.all()
    id1=[]
    ia=[]
    ne=[]
    co=[]
    ra=[]
    di=[]
    da=[]
    for i in a:
        w=i.id
        id1.append(w)
        l=str(i.cusimage).split('/')[-1]
        ia.append(l)
        k=i.cuname
        ne.append(k)
        u=i.comments
        co.append(u)
        m=i.deleplace
        ra.append(m)
        n=i.deldate
        di.append(n)
        o=i.occation
        da.append(o)
    ru=zip(id1,ia,ne,co,ra,di,da)
    return render(request,'homepagedisplay.html',{'ru':ru})


#review delete:admin or customer
def reviewdelete(request,id):
    w=reviewmodel.objects.get(id=id)
    os.remove(str(w.cusimage))
    w.delete()
    return redirect(reviewdisplayview)



# edit of review:customers only
def reviewedit(request,id):
    a=reviewmodel.objects.get(id=id)
    img=str(a.cusimage).split('/')[-1]
    if request.method=='POST':
        a.cuname=request.POST.get('cuname')
        a.comments=request.POST.get('comments')
        a.deleplace=request.POST.get('deleplace')
        a.occation=request.POST.get('occation')
        if request.POST.get('deldate')=='':
            a.save()
        else:
            a.deldate=request.POST.get('deldate')
        a.save()
        if len(request.FILES)!=0:
            if len(a.cusimage)>0:
                os.remove(a.cusimage.path)
            a.cusimage=request.FILES['cusimage']
        a.save()
        return redirect(reviewdisplayview)
    return render(request,'editreviewpage.html',{'a':a,'img':img})


# forgot password:views
def forgot_password(request):
    a=customerregmodel.objects.all()
    if request.method=='POST':
        em=request.POST.get('email')
        un=request.POST.get('uname')
        for i in a:
            if (i.email==em and i.uname==un):
                id=i.id
                subject="please change your password......."
                message=f"http://127.0.0.1:8000/main_app/changepassword/{id}"
                frm="ctpraseeda8064@gmail.com"
                to=em
                send_mail(subject,message,frm,[to])
                return HttpResponse("Please Check Your Mail..")
        else:
            return HttpResponse("Sorry...Please Try Again")
    return render(request,'forgotpswpage.html')



# passwordchange views:
def change_password(request,id):
    a=customerregmodel.objects.get(id=id)
    if request.method=='POST':
        ps=request.POST.get('passw')
        rs=request.POST.get('confpass')
        if ps==rs:
            a.passw=ps
            a.save()
            return redirect(thankyou)
        else:
            return HttpResponse("sorry....Some error occured...please check again...")
    return render(request,'changepassword.html')

#thankyou page:
def thankyou(request):
    return render(request,'thankyou.html')

#empty cart:
def emptycartitems(request):
    return render(request,'emptycard.html')


#empty wishlist:
def emptywishlistitems(request):
    return render(request,'emptywishlist.html')


#aboutus:
def aboutpage(request):
    return render(request,'aboutus.html')

#contactpage:
def contactpage(request):
    return render(request,'contact.html')

#terms and condition:
def termscondition(request):
    return render(request,'termsandcondition.html')
