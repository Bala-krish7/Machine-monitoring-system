from django.http import HttpResponse
from django.shortcuts import render
from sklearn.preprocessing import StandardScaler
import joblib
import numpy as np

def home(request):
    return render(request,"home.html")
def failureprediction(request):
    return render(request,"failureprediction.html")

def Oilanalysis(request):
    return render(request,"Oilanalysis.html")

def vib(request):
    return render(request,"vib.html")

def FCNN(request):
    return render(request,"FCNN.html")

def FRBFN(request):
    return render(request,"FRBFN.html")

def FSVC(request):
    return render(request,"FSVC.html")

def FXGB(request):
    return render(request,"FXGB.html")

def FLSTM(request):
    return render(request,"FLSTM.html")

def OXGB(request):
    return render(request,"OXGB.html")

def OLSTM(request):
    return render(request,"OLSTM.html")

def ONN(request):
    return render(request,"ONN.html")


def result(request):
    cls = joblib.load('finalmodel.sav')


    lis = []
    lis.append(float(request.GET['AT']))
    lis.append(float(request.GET['PT']))
    lis.append(float(request.GET['RS']))
    lis.append(float(request.GET['T']))
    lis.append(float(request.GET['TW']))
    lis.append(0)
    lis.append(0)
    lis.append(0)
    lis.append(0)
    lis.append(0)

    lis = np.array(lis)
    lis = lis.reshape(2,5)
    
    
    
    pred = cls.predict(lis)[0]
    if(pred<0.5):
        pred=0
    else:
        pred=1
    if(pred==0):
        ans="There is no failure in the machine"
    else:
        ans="There is a failure in the machine. \nCall for sevices"


    return render(request,"result.html",{'ans':ans})

def result1(request):
    cls = joblib.load('xgbmodel.sav')


    lis = []
    lis.append(float(request.GET['AT']))
    lis.append(float(request.GET['PT']))
    lis.append(float(request.GET['RS']))
    lis.append(float(request.GET['T']))
    lis.append(float(request.GET['TW']))
    lis.append(0)
    lis.append(0)
    lis.append(0)
    lis.append(0)
    lis.append(0)

    lis = np.array(lis)
    lis = lis.reshape(2,5)
    
    
    
    pred = cls.predict(lis)[0]
    if(pred==0):
        ans="There is no failure in the machine"
    else:
        ans="There is a failure in the machine. \nCall for sevices"


    return render(request,"result.html",{'ans':ans})

def result2(request):
    cls = joblib.load('svcmodel.sav')


    lis = []
    lis.append(float(request.GET['AT']))
    lis.append(float(request.GET['PT']))
    lis.append(float(request.GET['RS']))
    lis.append(float(request.GET['T']))
    lis.append(float(request.GET['TW']))
    lis.append(0)
    lis.append(0)
    lis.append(0)
    lis.append(0)
    lis.append(0)

    lis = np.array(lis)
    lis = lis.reshape(2,5)
    
    
    
    pred = cls.predict(lis)[0]
    if(pred==0):
        ans="There is no failure in the machine"
    else:
        ans="There is a failure in the machine. \nCall for sevices"


    return render(request,"result.html",{'ans':ans})

def result3(request):
    cls = joblib.load('lstm.sav')


    lis = []
    lis.append(float(request.GET['AT']))
    lis.append(float(request.GET['PT']))
    lis.append(float(request.GET['RS']))
    lis.append(float(request.GET['T']))
    lis.append(float(request.GET['TW']))
    lis.append(0)
    lis.append(0)
    lis.append(0)
    lis.append(0)
    lis.append(0)

    lis = np.array(lis)
    lis = lis.reshape(2,5)
    
    
    
    pred = cls.predict(lis)[0]

    if(pred<0.5):
        pred=0
    else:
        pred=1
    if(pred==0):
        ans="There is no failure in the machine"
    else:
        ans="There is a failure in the machine. \nCall for sevices"


    return render(request,"result.html",{'ans':ans})

def result4(request):
    cls = joblib.load('oilXGB.sav')


    lis = []
    lis.append(float(request.GET['AT']))
    lis.append(float(request.GET['PT']))
    lis.append(float(request.GET['RS']))
    lis.append(float(request.GET['T']))
    lis.append(float(request.GET['V']))
    lis.append(float(request.GET['TW']))
    lis.append(0)
    lis.append(0)
    lis.append(0)
    lis.append(0)
    lis.append(0)
    lis.append(0)

    lis = np.array(lis)
    lis = lis.reshape(2,6)
    
    
    
    pred = cls.predict(lis)[0]
    if(pred==0):
        ans="The oil is efficient to use. \nThere is no need to change the oil"
    else:
        ans="The oil is not efficient to use. \nPlease change the oil"


    return render(request,"result.html",{'ans':ans})

def result5(request):
    cls = joblib.load('oilLSTM.sav')


    lis = []
    lis.append(float(request.GET['AT']))
    lis.append(float(request.GET['PT']))
    lis.append(float(request.GET['RS']))
    lis.append(float(request.GET['T']))
    lis.append(float(request.GET['V']))
    lis.append(float(request.GET['TW']))
    lis.append(0)
    lis.append(0)
    lis.append(0)
    lis.append(0)
    lis.append(0)
    lis.append(0)

    lis = np.array(lis)
    lis = lis.reshape(2,6)
    
    
    
    pred = cls.predict(lis)[0]

    if(pred<0.5):
        pred=0
    else:
        pred=1
    if(pred==0):
        ans="The oil is efficient to use\nThere is no need to change the oil"
    else:
        ans="The oil is not efficient to use\nPlease change the oil"


    return render(request,"result.html",{'ans':ans})

def result6(request):
    cls = joblib.load('oilNN.sav')


    lis = []
    lis.append(float(request.GET['AT']))
    lis.append(float(request.GET['PT']))
    lis.append(float(request.GET['RS']))
    lis.append(float(request.GET['T']))
    lis.append(float(request.GET['V']))
    lis.append(float(request.GET['TW']))
    lis.append(0)
    lis.append(0)
    lis.append(0)
    lis.append(0)
    lis.append(0)
    lis.append(0)

    lis = np.array(lis)
    lis = lis.reshape(2,6)
    
    
    
    pred = cls.predict(lis)[0]

    if(pred<0.5):
        pred=0
    else:
        pred=1
    if(pred==0):
        ans="The oil is efficient to use\nThere is no need to change the oil"
    else:
        ans="The oil is not efficient to use\nPlease change the oil"


    return render(request,"result.html",{'ans':ans})

def result7(request):
    cls = joblib.load('FRBFN.sav')


    lis = []
    lis.append(float(request.GET['AT']))
    lis.append(float(request.GET['PT']))
    lis.append(float(request.GET['RS']))
    lis.append(float(request.GET['T']))
    lis.append(float(request.GET['TW']))
    lis.append(0)
    lis.append(0)
    lis.append(0)
    lis.append(0)
    lis.append(0)

    lis = np.array(lis)
    lis = lis.reshape(2,5)
    
    
    
    pred = cls.predict(lis)[0]

    if(pred<0.5):
        pred=0
    else:
        pred=1
    if(pred==0):
        ans="There is no failure in the machine"
    else:
        ans="There is a failure in the machine. \nCall for sevices"


    return render(request,"result.html",{'ans':ans})

