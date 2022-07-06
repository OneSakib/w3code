from .models import TutList
from MainApp.forms import NewUserForm
from MainApp.models import ArticleBookmark


def tut_list(request):
    context = {
        'object_list_tut': TutList.objects.all(),
        'registration_form': NewUserForm(),
        'article_obj': ArticleBookmark.objects
    }
    return context
