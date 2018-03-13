from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Project
from django.http import HttpResponse
import json
from collections import Counter
from operator import itemgetter


# Create your views here.
import math

def counter_cosine_similarity(c1, c2):
    terms = set(c1).union(c2)
    dotprod = sum(c1.get(k, 0) * c2.get(k, 0) for k in terms)
    magA = math.sqrt(sum(c1.get(k, 0)**2 for k in terms))
    magB = math.sqrt(sum(c2.get(k, 0)**2 for k in terms))
    return dotprod / (magA * magB)
@csrf_exempt
def search(request):
    query=request.POST.get('search','no')
    query=query.split()
    if 'video' in query:
        query.remove('video')

    
    lis1 =Project.objects.all()
    lis=[]
    
    for a in lis1:
        temp= a.keyword.split(',')
        
        
        
        if query[-1] in temp:
            counterA = Counter(temp)
            counterB = Counter(query)
            a.score=counter_cosine_similarity(counterA,counterB)
            a.save()
            lis.append(a)
            
        
    
    lis=sorted(lis,key=lambda x:x.score)
    dictionary={}
   
    for a in lis:
        dictionary[a.url]=a


    lis=lis[:4]
    
   
    
    
   
        
     
    
    
    result=[]
    for a in dictionary:
           
           
        
            d={}
            d['name']=dictionary[a].name
            d['url']=dictionary[a].url
            data=json.dumps(str(dictionary[a].photo))
            d['photo']=data
            d['score']=dictionary[a].score
            result.append(d)
    print(result)
     
   
    
    context={"search_result":result} 
    
     
    return JsonResponse(context)  


@csrf_exempt
def home_page(request):
  return render(request,"video.html")  
    
  
    
    
        
       
    
    




