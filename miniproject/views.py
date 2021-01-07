import os

import enchant
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def hotel(request):
    #taking value from html
    if request.method == "POST":
        txt = request.POST['Review']
        print(txt)
    #calling function
    id1="ID-0887"
    d=enchant.Dict("en_us")

    tc=0
    txt1=str(txt)
    txt1=txt.split(" ")
    if(not txt.strip()):
        pass
        #messagebox.showinfo("Sorry!", "Mandatory data missing")
    else:
        if len(txt1)<=3:
             print("Length is insufficient")
        else:
           # messagebox.showinfo("Thank You!", "Your review is successfully submitted. Please wait for the result.")
            file1=open("input.txt", 'w', encoding="utf")
            file1.write(id1 + '\t' +txt)
            file1.close()
            os.system("python VerifyReview.py")
            os.system("python ReviewTypeDetector.py")
            for i in txt1:
                if d.check(i) == True:
                    tc+=1
            res=tc/len(txt1)*100
            s1=""
            rev=""
            if res <=70 or len(txt1)<=10:
                s1="Fake"
            else:
                fileRead=open('Result.txt', "r", encoding="utf-8")
                s1=fileRead.read()
                fileRead.close()
                fileRead = open("Result-Type.txt", "r", encoding="utf-8")
                rev=fileRead.read()
                fileRead.close()
            s='Result: This review is '+s1+" "+rev
            print(s)
            content={'results': s}
    return render(request, 'hotel.html', content)

def product(request):
    # taking value from html
    if request.method == "POST":
        txt = request.POST['Review1']
        print(txt)
    # calling function
    id1 = "ID-0887"
    d = enchant.Dict("en_us")

    tc = 0
    txt1 = str(txt)
    txt1 = txt.split(" ")
    if (not txt.strip()):
        pass
        #messagebox.showinfo("Sorry!", "Mandatory data missing")
    else:
        if len(txt1) <= 3:
            print("Length is insufficient")
        else:
            #messagebox.showinfo("Thank You!", "Your review is successfully submitted. Please wait for the result.")
            file1 = open("input.txt", 'w', encoding="utf")
            file1.write(id1 + '\t' + txt)
            file1.close()
            os.system("python VerifyReview.py")
            os.system("python ReviewTypeDetector.py")
            for i in txt1:
                if d.check(i) == True:
                    tc += 1
            res = tc / len(txt1) * 100
            s1 = ""
            rev = ""
            if res <= 70 or len(txt1) <= 10:
                s1 = "Fake"
            else:
                fileRead = open('Result.txt', "r", encoding="utf-8")
                s1 = fileRead.read()
                fileRead.close()
                fileRead = open("Result-Type.txt", "r", encoding="utf-8")
                rev = fileRead.read()
                fileRead.close()
            s = 'Result: This review is ' + s1 + " " + rev
            print(s)
            content1 = {'results1': s}
    return render(request, 'product.html', content1)
