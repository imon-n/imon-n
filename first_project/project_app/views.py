from django.shortcuts import render
import datetime

def home(request):
    dictt = {'name' : 'imon' , 'age':6, 
    'to_day':datetime.datetime.now() , 'course' :[
        {
            'id' : 1,
            'course-name' : 'EEE',
            'students' : 40
        },
        {
            'id' : 2,
            'course-name' : 'CSE',
            'fee' : 80
        },
        {
            'id' : 3,
            'course-name' : 'Civil',
            'fee' : 27
        }
    ] , 'list' : ['Matlab', 'is', 'nice',54] , 'value':[
                                                        {'name': 'jakir', 'age': 19},
                                                        {'name': 'amina', 'age': 22},
                                                        {'name': 'imon', 'age': 31},
                                                    ]}

    return render(request,'index.html' , dictt)