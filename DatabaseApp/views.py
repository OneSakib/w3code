from django.shortcuts import HttpResponseRedirect
from django.views.generic import TemplateView, DetailView, FormView, View
from .forms import *
from django.urls import reverse_lazy
from next_prev import next_in_order, prev_in_order


# Create your views here.
class MYSqlView(View):
    def get(self, request):
        slug = MysqlDB.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Database:mysqldetail', kwargs={'slug': slug}))


class MySqlDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = MysqlDBCommentsForm
    model = MysqlDB

    def get_context_data(self, **kwargs):
        context = super(MySqlDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = MysqlDBComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Database:mysqldetail', kwargs={'slug': self.kwargs['slug']}))


class MongoDBView(View):
    def get(self, request):
        slug = MongoDB.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Database:mongodbdetail', kwargs={'slug': slug}))


class MongoDBDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = MongoDBCommentsForm
    model = MongoDB

    def get_context_data(self, **kwargs):
        context = super(MongoDBDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = MongoDBComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Database:mongodbdetail', kwargs={'slug': self.kwargs['slug']}))


class PostgreSqlView(View):
    def get(self, request):
        slug = PostgreSQLDB.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Database:postgresqldetail', kwargs={'slug': slug}))


class PostgreSQLDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = PostgreSQLDBCommentsForm
    model = PostgreSQLDB

    def get_context_data(self, **kwargs):
        context = super(PostgreSQLDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = PostgreSQLDBComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Database:postgresqldetail', kwargs={'slug': self.kwargs['slug']}))


class OracleView(View):
    def get(self, request):
        slug = OracleDB.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Database:oracledetail', kwargs={'slug': slug}))


class OracleDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = OracleDBCommentssForm
    model = OracleDB

    def get_context_data(self, **kwargs):
        context = super(OracleDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = OracleDBComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Database:oracledetail', kwargs={'slug': self.kwargs['slug']}))


class SqliteView(View):
    def get(self, request):
        slug = SqliteDB.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Database:sqlitedetail', kwargs={'slug': slug}))


class SqliteDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = SqliteDBCommentsForm
    model = SqliteDB

    def get_context_data(self, **kwargs):
        context = super(SqliteDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = SqliteDBComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Database:sqlitedetail', kwargs={'slug': self.kwargs['slug']}))


class MariaDBView(View):
    def get(self, request):
        slug = MariaDB.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Database:mariadbddetail', kwargs={'slug': slug}))


class MariaDBDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = MariaDBCommentsForm
    model = MariaDB

    def get_context_data(self, **kwargs):
        context = super(MariaDBDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = MariaDBComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Database:mariadbddetail', kwargs={'slug': self.kwargs['slug']}))
