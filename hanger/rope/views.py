from django.shortcuts import render
from .models import Cow, Milk

# Create your views here.

def index(request):
	c = Milk.objects.filter(pk=1)
	# for cm in c:
	# 	x = cm.cow_set.all()
	# 	for y in x:
	# 		print(y)
	for b in c:
		d = b.cow_set.all() 
		print(d)
	return render(request, 'blog.html', {})
    




def log(request):
	return render(request, 'log.html', {})
