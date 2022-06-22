from .models import TutList


def tut_list(request):
    return {'object_list': TutList.objects.all()}
