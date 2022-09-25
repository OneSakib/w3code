def get_object_pagination(model, cur_obj):
    obj = model.objects.all().order_by('parent')
    for i, o in enumerate(obj):
        if o == cur_obj:
            try:
                next = obj[i + 1]
            except Exception as e:
                next = None
            try:
                prev = obj[i - 1]
            except Exception as e:
                prev = None
            return next, prev
            break


def get_blog_object_pagination(model, cur_obj):
    obj = model.objects.all()
    for i, o in enumerate(obj):
        if o == cur_obj:
            try:
                next = obj[i + 1]
            except Exception as e:
                next = None
            try:
                prev = obj[i - 1]
            except Exception as e:
                prev = None
            return next, prev
            break
