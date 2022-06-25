from .models import TutList


def tut_list(request):
    return {'object_list_tut': TutList.objects.all()}
