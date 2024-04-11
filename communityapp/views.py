from django.shortcuts import redirect, render
from django.contrib import messages
from communityapp.models import DriverLoginDetails, Users, clothes, donation, foods,requestitem

# Create your views here.
def index(request):
    if 'EmailID' in request.session:
        current_user= request.session['EmailID']
        user=Users.objects.get(EmailID=current_user)
        return render(request,"index.html",{'user':user,'current_user':current_user})
    elif 'Email' in request.session:
        current_driver= request.session['Email']
        user=DriverLoginDetails.objects.get(Email=current_driver)
        return render(request,"index.html",{'user':user,'current_driver':current_driver})
    return render(request,"index.html")
def userregister(request):
    if request.method=='POST':
        name=request.POST['name']
        emailid=request.POST['Email']
        passw=request.POST['password']
        cpass=request.POST['cpassword']
        phone=request.POST['phone']
        address=request.POST['address']
        place=request.POST['place']
        emailexists=Users.objects.filter(EmailID=emailid)
        if emailexists:
            messages.error(request,"Email id already registered")
        elif passw!=cpass:
            messages.error(request,"Password does not match")
        else:
            Users.objects.create(Name=name,EmailID=emailid,Password=passw,Phone=phone,Address=address,Place=place)
            return redirect('/')
    return render(request,"userregister.html")
def userlogin(request):
    if request.method=='POST':
        emailid=request.POST['Email']
        passw=request.POST['password']
        user=Users.objects.filter(EmailID=emailid,Password=passw)
        if user:
            request.session['EmailID']=emailid
            return redirect('/')
        else:
            messages.error(request,"invalid credentials")
    return render(request,"userlogin.html")
def userlogout(request):
    if 'EmailID' in request.session:
        del request.session['EmailID']
        return redirect('/')
    elif 'Email' in request.session:
        del request.session['Email']
        return redirect('/')
def donationitems(request):
    if 'EmailID' in request.session:
        current_user= request.session['EmailID']
        user=Users.objects.get(EmailID=current_user)
        if request.method=='POST':
            name=request.POST['name']
            type=request.POST['donationtype']
            item=request.POST['item']
            qty=request.POST['quantity']
            desc=request.POST['address']
            loc=request.POST['location']
            contact=request.POST['phone']
            pic=request.FILES.get('image')
            if type=='food':
                donation.objects.create(Name=name,Type_of_donation=type,Item=item,Quantity=qty,Description=desc,Location=loc,Contact_no=contact,Pic=pic)
                foods.objects.create(Name=name,Item=item,Quantity=qty,Description=desc,Location=loc,Contact_no=contact,Pic=pic)
                return redirect('/')
            else:
                donation.objects.create(Name=name,Type_of_donation=type,Item=item,Quantity=qty,Description=desc,Location=loc,Contact_no=contact,Pic=pic)
                clothes.objects.create(Name=name,Item=item,Quantity=qty,Description=desc,Location=loc,Contact_no=contact,Pic=pic)
                return redirect('/')
        return render(request,"donationform.html",{'user':user,'current_user':current_user})
    return render(request,"donationform.html")
def profile(request):
    if 'EmailID' in request.session:
        return render(request,"profile.html")
    else:
        return redirect('/')
def personal(request):
    if 'EmailID' in request.session:
        current_user= request.session['EmailID']
        user=Users.objects.get(EmailID=current_user)
        return render(request,"myprofile.html",{'user':user,'current_user':current_user})
def updateprofile(request):
    if 'EmailID' in request.session:
        current_user= request.session['EmailID']
        user=Users.objects.get(EmailID=current_user)
        if request.method=='POST':
            name=request.POST['name']
            passw=request.POST['password']
            cpass=request.POST['cpassword']
            phone=request.POST['phone']
            address=request.POST['address']
            place=request.POST['place']
            if passw!=cpass:
                messages.error(request,"Password does not match")
            else:
                user.Name=name
                user.Password=passw
                user.Phone=phone
                user.Address=address
                user.Place=place
                user.save()
                return redirect('personal')
        return render(request,"updateprofile.html",{'user':user,'current_user':current_user})
def donation_history(request):
    if 'EmailID' in request.session:
        current_user= request.session['EmailID']
        user=Users.objects.get(EmailID=current_user)
        donate=donation.objects.filter(Name=user.EmailID)
        return render(request,"donationhistory.html",{'user':user,'current_user':current_user,'donate':donate})
def donation_items(request):
    return render(request,"donateitem.html")
def fooditems(request):
    item=foods.objects.all()
    return render(request,"foods.html",{'item':item})
def clothitems(request):
    item=clothes.objects.all()
    return render(request,"clothes.html",{'item':item})
def requestitems(request):
    if 'EmailID' in request.session:
        current_user= request.session['EmailID']
        user=Users.objects.get(EmailID=current_user)
        if request.method=='POST':
            email=request.POST['email']
            type=request.POST['requesttype']                    
            item=request.POST['item']
            qty=request.POST['quantity']
            loc=request.POST['location']
            ph=request.POST['phone']
            requestitem.objects.create(Email=email,ItemType=type,ItemName=item,Quantity=qty,Location=loc,PhoneNumber=ph)
            return redirect('/')
        return render(request,"requestform.html",{'user':user,'current_user':current_user})
    else:
        return redirect('userlogin')
def requesthistory(request):
    if 'EmailID' in request.session:
        current_user= request.session['EmailID']
        user=Users.objects.get(EmailID=current_user)
        item=requestitem.objects.filter(Email=user.EmailID)
        item1=DriverLoginDetails.objects.filter(Email=user.EmailID)
        return render(request,"requesthistory.html",{'user':user,'current_user':current_user,'item':item,'item1':item1})
def driverlogin(request):
    if request.method=='POST':
        emailid=request.POST['Email']
        passw=request.POST['password']
        user=DriverLoginDetails.objects.filter(Email=emailid,Password=passw)
        if user:
            request.session['Email']=emailid
            return redirect('driverprofile')
        else:
            messages.error(request,"invalid credentials")
    return render(request,"driverlogin.html")
def driverprofile(request):
    if 'Email' in request.session:
        current_user= request.session['Email']
        user=DriverLoginDetails.objects.get(Email=current_user)
        work=requestitem.objects.filter(Location=user.PlaceAllocation)
        return render(request,"driverprofile.html",{'user':user,'current_user':current_user,'works':work})
    return render(request,"driverprofile.html")
def onthewayupdate(request,place):
    det=DriverLoginDetails.objects.get(PlaceAllocation=place)
    det.Status="on the way"
    det.save()
    return redirect('driverprofile')
def deliveredupdate(request,place):
    det=DriverLoginDetails.objects.get(PlaceAllocation=place)
    det.Status="delivered"
    det.save()
    return redirect('driverprofile')
def statusupdate(request,id):
    det=requestitem.objects.get(id=id)
    det.Status="success"
    det.save()
    return redirect('driverprofile')
def status1update(request,id):
    det=requestitem.objects.get(id=id)
    det.Status="declined"
    det.save()
    return redirect('driverprofile')
def deletedonateitem(request,id):
    donate=donation.objects.get(id=id)
    if donate.Type_of_donation == 'food':
        donat=foods.objects.get(Name=donate.Name)
        donat.delete()
    elif donate.Type_of_donation == 'cloth':
        donat=clothes.objects.get(Name=donate.Name)
        donat.delete()
    donate.delete()
    return redirect('/')
def deleterequestitem(request,id):
    donate=requestitem.objects.get(id=id)
    donate.delete()
    return redirect('/')   