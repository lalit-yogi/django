from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
	return render(request,"homepage.html",{"title":"Word count website"})

def contact(request):
	return HttpResponse("<h2>this is contact us page</h1>This is test content only")


def count(request):
	data = request.POST["word"]
	data_list = data.split()
	data_len = len(data_list)
	worddics = {}
	for word in data_list:
		if word in worddics:
			worddics[word] +=1
		else:
		    worddics[word] =1
	sortlist = sorted(worddics.items(),key=operator.itemgetter(1),reverse=True)	    	
	return render(request,"count.html",{"data":data,"data_len":data_len,"data_frequency":sortlist})