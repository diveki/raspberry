from django.shortcuts import render

# Create your views here.
def index(request):
    """View function for home page of site."""

    context = {}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'main.html', context=context)

def kurzusok(request):
    """View function for home page of site."""

    context = {}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'kurzusok.html', context=context)

def kurzus1(request):
    content = 'To be determined ...'
    context = {'title': 'Kurzus 1',
                'introduction': 'Sok sok bla bla',
                'age': '10- ...',
                'duration': '1.5 h',
                'equipments': 'Everything is provided',
                'prerequisit': 'Semmi',
                'content': content}
    return render(request, 'kurzus_reszletes.html', context=context)

def kurzus2(request):
    content = 'To be determined ...'
    context = {'title': 'Kurzus 2',
                'introduction': 'Sok sok bla bla',
                'age': '10-...',
                'duration': '1.5 h',
                'equipments': 'Everything is provided',
                'prerequisit': 'Kurzus 1',
                'content': content}
    return render(request, 'kurzus_reszletes.html', context=context)

def kurzus3(request):
    content = 'To be determined ...'
    context = {'title': 'Kurzus 3',
                'introduction': 'Sok sok bla bla',
                'age': '10-...',
                'duration': '1.5 h',
                'equipments': 'Everything is provided',
                'prerequisit': 'Kurzus 2',
                'content': content}
    return render(request, 'kurzus_reszletes.html', context=context)

def kurzus4(request):
    content = 'To be determined ...'
    context = {'title': 'Kurzus 4',
                'introduction': 'Sok sok bla bla',
                'age': '10-...',
                'duration': '1.5 h',
                'equipments': 'Everything is provided',
                'prerequisit': 'Kurzus 3',
                'content': content}
    return render(request, 'kurzus_reszletes.html', context=context)

def iskolak(request):
    items = [{'city': 'Szeged', 'address': 'Eli-Alps, 6728 Szeged, Wolfgang Sandner utca 3', 'link': ''},
              {'city': 'Budapest', 'address': '1211 Budapest, Petofi Sandor utca 12', 'link': ''},
              {'city': 'Algyő', 'address': '6750 Algyő, Tiszavvirág utca 27', 'link': ''}
              ]
    context = {'items': items}
    return render(request, 'iskolak.html', context = context)

inspiracio = [
    {'title': 'Fingo parna', 'user': 'picur', 'likes_count': 12, 'views_count': 100, 'abstract': 'Ez egy projekt a fingoparnarol.', 'link': ''},
    {'title': 'Fingo parna', 'user': 'picur', 'likes_count': 12, 'views_count': 100, 'abstract': 'Ez egy projekt a fingoparnarol.', 'link': ''},
    {'title': 'Fingo parna', 'user': 'picur', 'likes_count': 12, 'views_count': 100, 'abstract': 'Ez egy projekt a fingoparnarol.', 'link': ''},
]

def inspiraciok(request):
    context = {'items': inspiracio}
    return render(request, 'inspiracio.html', context = context)

def kapcsolat(request):
    context = {}
    return render(request, 'kapcsolat.html', context = context)