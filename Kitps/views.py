from django.http import HttpResponse ,HttpResponseRedirect
# from django.shortcuts  import render,get_object_or_404
from .forms import userForm
from service.models import Services
from news.models import News
from django.core.paginator import Paginator
from contactinquiry.models import ContactInquiry
from django.core.mail import send_mail,EmailMultiAlternatives
from course.models import Course
from django.shortcuts  import render,get_object_or_404


from django.db.models import Q

#------- Multiple user ko email send krne ke liye "EmailMultiAlternatives"  ka use krenge------


# 1.'subject here' : measn kis kaam ke liye use kr rahe ho
# 2."Here is the message.": jo bhi message bhejna hai vo yaha likhen
# 3."from@example.com":   konsi 'email id' use krkr mesage bhejna hai  
# 4. ["to@example.com"]:  kiste pass mail bhejna hai use persion ki 'email id'
# 5. fail_silently=False:
# )

def HomePage(request): 
    
    # USE OF EmailMultiAlternatives MULTIPLE USER KO MAIL SEND KRNE KE LIYE
    #  msg=EmailMultiAlternatives(subject,msg,from_mail,[to,Multiple email add kr sakte hai like arun@123,jatin@123, varun@124 etc])

#     send_mail(
#     "AD-AxisBk",    
#     "Rs.10000.00 is Debited to A/c XX1234 on 25-03-2026 00:11:12 (Clear Bal Rs.0.00) by UPI Ref:DR/7894561230-AXIS. Urgent: If not done by you, call customer care immediately.",
#     "sagarrv29@gmail.com",
#     ["29kamalchaap123@gmail.com "],
#     fail_silently=False,
# )

    
    # subject="AD-AxisBk",    
    # msg="Rs.10000.00 is Debited to A/c XX1234 on 25-03-2026 00:11:12 (Clear Bal Rs.0.00) by UPI Ref:DR/7894561230-AXIS. Urgent: If not done by you, call customer care immediately.",
    # from_mail="sagarrv29@gmail.com",
    # to=["29kamalchaap123@gmail.com "],
    # msg=EmailMultiAlternatives(subject,msg,from_mail,[to])
    # msg.content_subtype='html'
    # msg.send()

    newsData=News.objects.all();
    
    name = request.GET.get('name', '')
    email = request.GET.get('email', '')
    phone = request.GET.get('phone', '')
   
    context = {
        'newsData':newsData,
        'name': name,
        'email': email,
        'phone': phone
    }
    return render(request, "index.html", context)

def search(request):
    query = request.GET.get('q')
    
    course_results = []
    
    service_results = []
    news_results=[]

    if query:
        course_results = Course.objects.filter(
            Q(course_title__icontains=query) |
            
            Q(course_desc__icontains=query)  |
            Q(duration__icontains=query) |
            Q(fees__icontains=query) |
            Q(eligibility__icontains=query)
        )[:10]

        

        service_results = Services.objects.filter(
            Q(service_heading__icontains=query)|
            Q(service_button__icontains=query)|
            Q(service_desc__icontains=query)
            
        )[:10]

        news_results = News.objects.filter(
            Q(news_title__icontains=query) |
            Q(news_description__icontains=query) 
        )[:10]
        print("Query:", query)
        print("Courses:", course_results)
        print("Services:", service_results)
        print("News:", news_results)
    context = {
        'query': query,
        'course_results': course_results,
        
        'service_results': service_results,
        'news_results' : news_results
    }

    return render(request, 'search.html', context)
def newDetails(request,slugs):
    newDetails=News.objects.get(news_slugs=slugs)
    Data={
        'newDetails': newDetails

    }
    return render(request,"NewsDetail.html",Data)
def AboutPage(request):
    course=Course.objects.all()
    return render(request,"About.html",{'course':course})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, 'course_detail.html', {'course': course})

def ContactPage(request):
    
    return render(request,"Contact.html")
def saveInquiry(request):
    
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        course=request.POST.get('course')
        qualification=request.POST.get('qualification')
        city=request.POST.get('city')
        message=request.POST.get('message')



        saveData=ContactInquiry(name=name,email=email,phone=phone,course=course,qualification=qualification,city=city,message=message)
        saveData.save()
        # Response='Thank you for submitting your admission application.<br> Your details have been successfully received and <br>are currently under review by our admissions team. We will contact you soon regarding the next steps in the admission process.'
    return render(request,"Response.html")
def NewsPage(request):
    return render(request,"news.html")
def marksheet(request):
    Total = ''
    Percentage=''
    error=''
    try:
        if request.method=='POST':
            EM=int(request.POST.get('num1'))
            HM=int(request.POST.get('num2'))
            MM=int(request.POST.get('num3'))
            SM=int(request.POST.get('num4'))
            SSM=int(request.POST.get('num5'))
            DM=int(request.POST.get('num6'))
            Total=EM+HM+MM+SM+SSM+DM
            Percentage=Total/6

            if Percentage>=75:
                Division='A'
            elif Percentage>=60:
                Division='B'
            elif Percentage>=40:
                Division='c'  
            else:
                Division='Fail'      
    except ValueError:
        error= "Invalid input! Please enter valid numbers."
    context={'Total':Total,
             'Percentage': Percentage,
             'Division':Division,
             'error': error
             
             }    
    
    return render(request,'Marksheet.html',context)
def evenodd(request):
    result = ''
    if request.method=='POST':
        
        if request.POST.get('num1') =='':
             return render(request,'evenodd.html', {'error':True})

        n1=int(request.POST.get('num1'))
        if n1%2==0:
            result =  "It's a even number"
        else:
            result =  "It's a odd number"
    return render(request,'evenodd.html', {'result':result})           
def Calculator(request):
    C=''
    try:
        if request.method =='POST':
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            OPR=request.POST.get('Opr')
            if OPR =='+':
                C=n1+n2
            elif OPR =='-':
                C=n1-n2  
            elif OPR =='*':
                C=n1*n2  
            elif OPR =='/':
                C=n1/n2  
                if n2 ==0:
                    C="Can't divide by zero"
                else:
                    C = "Invalid Operator"    

    except:   
        C='Invalid choice.Please Try Again'   
    return render(request,'Calculator.html',{'C':C})
def EventsPage(request):
    #   use of this word search data  in only one charractor using this keyword '__icontains'
    ServiceData=Services.objects.all()
    
    # if request.method=="GET":
    #     st=request.GET.get('eventname')
    #     if st!=None:
    #         ServiceData=Services.objects.filter(service_heading__icontains=st)
   # django dose not allow  negative indexinglike [-1:],[::-1] etc
    context={
        'ServiceData':ServiceData 
    }

    return render(request,"events.html",context)
# def SubmitForm(request):
#    try: 
#      if request.method == "POST":
#         s1 = request.POST.get('name', '')
#         s2 = request.POST.get('email', '')
#         s3 = request.POST.get('phone', '')

#         li=[s1, s2, s3]
        
#         url=f"/?name={s1}&email={s2}&phone={s3}"

#         return HttpResponseRedirect(url)
#    except:
#        pass

def UserForm(request):
    
    fn=userForm()
    data={'form':fn}
    if request.method == "POST":
        s1 = request.POST.get('name', '')
        s2 = request.POST.get('email', '')
        s3 = request.POST.get('phone', '')

        li=[s1, s2, s3]
        data={
            'form':fn
        }
        url=f"/?name={s1}&email={s2}&phone={s3}"

        return HttpResponseRedirect(url)

    return render(request, "Userform.html",data)

