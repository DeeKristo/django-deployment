from django.shortcuts import render
from fib import mat_mul,mat_power,A,v
import time

# Create your views here.
def index(request):
    return render(request,'calc_fibonacci/index.html')

def result(request):
    if request.method == 'POST':
        input = int(request.POST.get('input'))
        start_time = time.time()
        output = mat_mul(mat_power(A,input-1),v)[0]
        total_time = time.time()-start_time
    return render(request,'calc_fibonacci/results.html',{'output':output,'time':total_time})
