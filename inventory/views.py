from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
# Create your views here.
import json
from .models import products


def get_all_items(request,*args,**kwargs):
    objects=pd.DataFrame(products.objects.all().values())
    # objects.drop('id')
    allcategory=objects['category'].unique()
    allout = {}
    for cat in allcategory:
        tempi = objects[objects['category']==cat]
        allout[cat]=tempi.to_dict()
        tempi=pd.DataFrame()
    return HttpResponse(json.dumps(allout))
    pass
