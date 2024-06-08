from django.shortcuts import render
from django.http import HttpResponse
import datetime

def fibbonacci(n):
    sequence = [0,1]
    while len(sequence)<n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def index(request):
    curr_time = datetime.datetime.now()
    # return HttpResponse(f"Hello, world! from Abhishek Verma\nThe time is: {curr_time.strftime('%Y-%m-%d %H:%M:%S')}")
    return HttpResponse(map(str,fibbonacci(10)))