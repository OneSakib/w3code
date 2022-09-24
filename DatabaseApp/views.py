from django.shortcuts import HttpResponseRedirect
from django.views.generic import TemplateView, DetailView, View
from .models import *
from django.urls import reverse_lazy
from next_prev import next_in_order, prev_in_order
from django.http import JsonResponse
from django.contrib.auth.models import User
from MainApp.views import CACHE_TTL, cache
from MainApp.functions import *

# Create your views here.
class MYSqlView(View):
    def get(self, request):
        slug = MysqlDB.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Database:mysqldetail', kwargs={'slug': slug}))


class MySqlDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Mysqlmodel') and cache.get('Mysqlparent_obj'):
        model = cache.get('Mysqlmodel')
        parent_obj = cache.get('Mysqlparent_obj')
    else:
        model = MysqlDB
        parent_obj = MySqlDBParent
        cache.set('Mysqlmodel', model)
        cache.set('Mysqlparent_obj', parent_obj)

    like_obj = MysqlDBLike

    def get_context_data(self, **kwargs):
        context = super(MySqlDetailView, self).get_context_data(**kwargs)
        obj_list = self.parent_obj.objects.all()
        context['obj_list'] = obj_list
        # Like Button
        context['obj_like_count'] = self.like_obj.objects.all().count()
        if self.request.user.is_authenticated:
            user = User.objects.get(username=self.request.user)
            if self.like_obj.objects.filter(user=user, post=self.object).exists():
                context['obj_like_exist'] = "Yes"
        else:
            context['obj_like_exist'] = "No"
        context['title'] = 'MySQL'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, **kwargs):
        pk = request.POST.get('pk')
        user = User.objects.get(username=request.user)
        context = {}
        if self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk)).exists():
            o = self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk))
            o.delete()
            context['ok'] = 'delete'
        else:
            self.like_obj.objects.create(user=user, post=self.model.objects.get(pk=pk))
            context['ok'] = 'create'
        context['number'] = self.like_obj.objects.all().count()
        return JsonResponse(context)


class MongoDBView(View):
    def get(self, request):
        slug = MongoDB.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Database:mongodbdetail', kwargs={'slug': slug}))


class MongoDBDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Mongomodel') and cache.get('Mongoparent_obj'):
        model = cache.get('Mongomodel')
        parent_obj = cache.get('Mongoparent_obj')
    else:
        model = MongoDB
        parent_obj = MongoDBParent
        cache.set('Mongomodel', model)
        cache.set('Mongoparent_obj', parent_obj)
    like_obj = MongoDBLike

    def get_context_data(self, **kwargs):
        context = super(MongoDBDetailView, self).get_context_data(**kwargs)
        obj_list = self.parent_obj.objects.all()
        context['obj_list'] = obj_list
        # Like Button
        context['obj_like_count'] = self.like_obj.objects.all().count()
        if self.request.user.is_authenticated:
            user = User.objects.get(username=self.request.user)
            if self.like_obj.objects.filter(user=user, post=self.object).exists():
                context['obj_like_exist'] = "Yes"
        else:
            context['obj_like_exist'] = "No"
        context['title'] = 'MongoDB'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, **kwargs):
        pk = request.POST.get('pk')
        user = User.objects.get(username=request.user)
        context = {}
        if self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk)).exists():
            o = self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk))
            o.delete()
            context['ok'] = 'delete'
        else:
            self.like_obj.objects.create(user=user, post=self.model.objects.get(pk=pk))
            context['ok'] = 'create'
        context['number'] = self.like_obj.objects.all().count()
        return JsonResponse(context)


class PostgreSqlView(View):
    def get(self, request):
        slug = PostgreSQLDB.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Database:postgresqldetail', kwargs={'slug': slug}))


class PostgreSQLDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Postgremodel') and cache.get('Postgreparent_obj'):
        model = cache.get('Postgremodel')
        parent_obj = cache.get('Postgreparent_obj')
    else:
        model = PostgreSQLDB
        parent_obj = PostgreSQLDBParent
        cache.set('Postgremodel', model)
        cache.set('Postgreparent_obj', parent_obj)
    like_obj = PostgreSQLDBLike

    def get_context_data(self, **kwargs):
        context = super(PostgreSQLDetailView, self).get_context_data(**kwargs)
        obj_list = self.parent_obj.objects.all()
        context['obj_list'] = obj_list
        # Like Button
        context['obj_like_count'] = self.like_obj.objects.all().count()
        if self.request.user.is_authenticated:
            user = User.objects.get(username=self.request.user)
            if self.like_obj.objects.filter(user=user, post=self.object).exists():
                context['obj_like_exist'] = "Yes"
        else:
            context['obj_like_exist'] = "No"
        context['title'] = 'PostgreSQL'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, **kwargs):
        pk = request.POST.get('pk')
        user = User.objects.get(username=request.user)
        context = {}
        if self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk)).exists():
            o = self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk))
            o.delete()
            context['ok'] = 'delete'
        else:
            self.like_obj.objects.create(user=user, post=self.model.objects.get(pk=pk))
            context['ok'] = 'create'
        context['number'] = self.like_obj.objects.all().count()
        return JsonResponse(context)


class OracleView(View):
    def get(self, request):
        slug = OracleDB.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Database:oracledetail', kwargs={'slug': slug}))


class OracleDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Oraclemodel') and cache.get('Oracleparent_obj'):
        model = cache.get('Oraclemodel')
        parent_obj = cache.get('Oracleparent_obj')
    else:
        model = OracleDB
        parent_obj = OracleDBParent
        cache.set('Oraclemodel', model)
        cache.set('Oracleparent_obj', parent_obj)
    like_obj = OracleDBLike

    def get_context_data(self, **kwargs):
        context = super(OracleDetailView, self).get_context_data(**kwargs)
        obj_list = self.parent_obj.objects.all()
        context['obj_list'] = obj_list
        # Like Button
        context['obj_like_count'] = self.like_obj.objects.all().count()
        if self.request.user.is_authenticated:
            user = User.objects.get(username=self.request.user)
            if self.like_obj.objects.filter(user=user, post=self.object).exists():
                context['obj_like_exist'] = "Yes"
        else:
            context['obj_like_exist'] = "No"
        context['title'] = 'Oracle'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, **kwargs):
        pk = request.POST.get('pk')
        user = User.objects.get(username=request.user)
        context = {}
        if self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk)).exists():
            o = self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk))
            o.delete()
            context['ok'] = 'delete'
        else:
            self.like_obj.objects.create(user=user, post=self.model.objects.get(pk=pk))
            context['ok'] = 'create'
        context['number'] = self.like_obj.objects.all().count()
        return JsonResponse(context)


class SqliteView(View):
    def get(self, request):
        slug = SqliteDB.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Database:sqlitedetail', kwargs={'slug': slug}))


class SqliteDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Sqlitemodel') and cache.get('Sqliteparent_obj'):
        model = cache.get('Sqlitemodel')
        parent_obj = cache.get('Sqliteparent_obj')
    else:
        model = SqliteDB
        parent_obj = SqliteDBParent
        cache.set('Sqlitemodel', model)
        cache.set('Sqliteparent_obj', parent_obj)
    like_obj = SqliteDBLike

    def get_context_data(self, **kwargs):
        context = super(SqliteDetailView, self).get_context_data(**kwargs)
        obj_list = self.parent_obj.objects.all()
        context['obj_list'] = obj_list
        # Like Button
        context['obj_like_count'] = self.like_obj.objects.all().count()
        if self.request.user.is_authenticated:
            user = User.objects.get(username=self.request.user)
            if self.like_obj.objects.filter(user=user, post=self.object).exists():
                context['obj_like_exist'] = "Yes"
        else:
            context['obj_like_exist'] = "No"
        context['title'] = 'SQLite'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, **kwargs):
        pk = request.POST.get('pk')
        user = User.objects.get(username=request.user)
        context = {}
        if self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk)).exists():
            o = self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk))
            o.delete()
            context['ok'] = 'delete'
        else:
            self.like_obj.objects.create(user=user, post=self.model.objects.get(pk=pk))
            context['ok'] = 'create'
        context['number'] = self.like_obj.objects.all().count()
        return JsonResponse(context)


class MariaDBView(View):
    def get(self, request):
        slug = MariaDB.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Database:mariadbddetail', kwargs={'slug': slug}))


class MariaDBDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Mariamodel') and cache.get('Mariaparent_obj'):
        model = cache.get('Mariamodel')
        parent_obj = cache.get('Mariaparent_obj')
    else:
        model = MariaDB
        parent_obj = MariaDBParent
        cache.set('Mariamodel', model)
        cache.set('Mariaparent_obj', parent_obj)
    like_obj = MariaDBLike

    def get_context_data(self, **kwargs):
        context = super(MariaDBDetailView, self).get_context_data(**kwargs)
        obj_list = self.parent_obj.objects.all()
        context['obj_list'] = obj_list
        # Like Button
        context['obj_like_count'] = self.like_obj.objects.all().count()
        if self.request.user.is_authenticated:
            user = User.objects.get(username=self.request.user)
            if self.like_obj.objects.filter(user=user, post=self.object).exists():
                context['obj_like_exist'] = "Yes"
        else:
            context['obj_like_exist'] = "No"
        context['title'] = 'MariaDB'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, **kwargs):
        pk = request.POST.get('pk')
        user = User.objects.get(username=request.user)
        context = {}
        if self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk)).exists():
            o = self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk))
            o.delete()
            context['ok'] = 'delete'
        else:
            self.like_obj.objects.create(user=user, post=self.model.objects.get(pk=pk))
            context['ok'] = 'create'
        context['number'] = self.like_obj.objects.all().count()
        return JsonResponse(context)
