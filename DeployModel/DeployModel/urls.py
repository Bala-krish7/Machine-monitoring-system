from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.home,name="home"),
    path('result/',views.result,name="result"),
    path('failureprediction/',views.failureprediction,name="failurepredicion"),
    path('Oilanalysis/',views.Oilanalysis,name="Oilanalysis"),
    path('Oilanalysis/OXGB',views.OXGB,name="OXGB"),
    path('Oilanalysis/OLSTM',views.OLSTM,name="OLSTM"),
    path('Oilanalysis/ONN',views.ONN,name="ONN"),
    path('vib/',views.vib,name="vib"),
    path('failureprediction/FCNN',views.FCNN,name="FCNN"),
    path('failureprediction/FRBFN',views.FRBFN,name="FRBFN"),
    path('failureprediction/FSVC',views.FSVC,name="FSVC"),
    path('failureprediction/FXGB',views.FXGB,name="FXGB"),
    path('failureprediction/FLSTM',views.FLSTM,name="FLSTM"),
    path('result1/',views.result1,name="result1"),
    path('result2/',views.result2,name="result2"),
    path('result3/',views.result3,name="result3"),
    path('result4/',views.result4,name="result4"),
    path('result5/',views.result5,name="result5"),
    path('result6/',views.result6,name="result6"),
    path('result7/',views.result7,name="result7")
]