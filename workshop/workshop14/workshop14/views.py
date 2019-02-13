from django.shortcuts import render


def info(request):
    return render(request,"info.html")
    
def student(request, name:
    s_dict = {
        "홍길동":22,
        "김길동":23,
    }
    age = s_dict.get[name]
    return render(request,"student.html",{"name":name,"age"=age})