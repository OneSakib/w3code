from .models import TutList
from MainApp.forms import NewUserForm
from MainApp.models import ArticleBookmark
from MainApp.views import CACHE_TTL, cache


def tut_list(request):
    if cache.get('object_list_tut') and cache.get('registration_form'):
        object_list_tut = cache.get('object_list_tut')
        registration_form = cache.get('registration_form')
    else:
        object_list_tut = TutList
        registration_form = NewUserForm
        cache.set('object_list_tut', object_list_tut)
        cache.set('registration_form', registration_form)

    context = {
        'object_list_tut': object_list_tut.objects.all(),
        'registration_form': registration_form(),
        'article_obj': ArticleBookmark.objects
    }

    return context
