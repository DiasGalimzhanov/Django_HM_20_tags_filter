from django.shortcuts import render

def home(request):
    users = [
        {
            'id': 1,
            'name': 'john',
            'age': 30,
            'city': 'New York',
        },
        {
            'id': 2,
            'name': 'jane',
            'age': 25,
            'city': 'London',
            'country': 'UK'
        },
        {
            'id': 3,
            'name': 'bob',
            'age': 35,
            'city': 'Paris',
            'country': 'France'
        },
        {
            'id': 4,
            'name': 'Alice',
            'age': 40,
            'city': 'Berlin',
            'country': 'Germany'
        },
    ]
    return render(request, 'home.html', {'users': users})
