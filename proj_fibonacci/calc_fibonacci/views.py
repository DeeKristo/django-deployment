from django.shortcuts import render
from fib import mat_mul,mat_power,A,v
import time

# Create your views here.
def index(request):
    return render(request,'calc_fibonacci/index.html')

def result(request):
    start_time = time.time()
    if request.method == 'POST':
        input = int(request.POST.get('input'))
        if input == 1:
            output = 1
        else:
            output = mat_mul(mat_power(A,input-1),v)[0]
        total_time = time.time()-start_time
        total_time = '{:.6f}'.format(total_time)
    return render(request,'calc_fibonacci/results.html',{'output':output,'time':total_time})
