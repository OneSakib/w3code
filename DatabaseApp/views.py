from django.shortcuts import HttpResponseRedirect
from django.views.generic import TemplateView, DetailView, View
from .models import *
from django.urls import reverse_lazy
from next_prev import next_in_order, prev_in_order


# Create your views here.
class MYSqlView(View):
    def get(self, request):
        slug = MysqlDB.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Database:mysqldetail', kwargs={'slug': slug}))


class MySqlDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = MysqlDB

    def get_context_data(self, **kwargs):
        context = super(MySqlDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'MySQL'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        currentpost = self.object
        prev = prev_in_order(currentpost)
        next = next_in_order(currentpost)
        context['prev'] = None
        context['next'] = None
        if prev != None:
            context['prev'] = prev
        if next != None:
            context['next'] = next
        return context


class MongoDBView(View):
    def get(self, request):
        slug = MongoDB.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Database:mongodbdetail', kwargs={'slug': slug}))


class MongoDBDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = MongoDB

    def get_context_data(self, **kwargs):
        context = super(MongoDBDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'MongoDB'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        currentpost = self.object
        prev = prev_in_order(currentpost)
        next = next_in_order(currentpost)
        context['prev'] = None
        context['next'] = None
        if prev != None:
            context['prev'] = prev
        if next != None:
            context['next'] = next
        return context


class PostgreSqlView(View):
    def get(self, request):
        slug = PostgreSQLDB.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Database:postgresqldetail', kwargs={'slug': slug}))


class PostgreSQLDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = PostgreSQLDB

    def get_context_data(self, **kwargs):
        context = super(PostgreSQLDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'PostgreSQL'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        currentpost = self.object
        prev = prev_in_order(currentpost)
        next = next_in_order(currentpost)
        context['prev'] = None
        context['next'] = None
        if prev != None:
            context['prev'] = prev
        if next != None:
            context['next'] = next
        return context


class OracleView(View):
    def get(self, request):
        slug = OracleDB.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Database:oracledetail', kwargs={'slug': slug}))


class OracleDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = OracleDB

    def get_context_data(self, **kwargs):
        context = super(OracleDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Oracle'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        currentpost = self.object
        prev = prev_in_order(currentpost)
        next = next_in_order(currentpost)
        context['prev'] = None
        context['next'] = None
        if prev != None:
            context['prev'] = prev
        if next != None:
            context['next'] = next
        return context


class SqliteView(View):
    def get(self, request):
        slug = SqliteDB.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Database:sqlitedetail', kwargs={'slug': slug}))


class SqliteDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = SqliteDB

    def get_context_data(self, **kwargs):
        context = super(SqliteDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'SQLite'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        currentpost = self.object
        prev = prev_in_order(currentpost)
        next = next_in_order(currentpost)
        context['prev'] = None
        context['next'] = None
        if prev != None:
            context['prev'] = prev
        if next != None:
            context['next'] = next
        return context


class MariaDBView(View):
    def get(self, request):
        slug = MariaDB.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Database:mariadbddetail', kwargs={'slug': slug}))


class MariaDBDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = MariaDB

    def get_context_data(self, **kwargs):
        context = super(MariaDBDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'MariaDB'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        currentpost = self.object
        prev = prev_in_order(currentpost)
        next = next_in_order(currentpost)
        context['prev'] = None
        context['next'] = None
        if prev != None:
            context['prev'] = prev
        if next != None:
            context['next'] = next
        return context
