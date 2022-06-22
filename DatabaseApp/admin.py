from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(MysqlDB)
class MysqlDBAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(MongoDB)
class MongoDBAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(PostgreSQLDB)
class PostgreSQLDBAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(OracleDB)
class OracleDBAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(SqliteDB)
class SqliteDBAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(MariaDB)
class MariaDBAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


# Comments
@admin.register(MysqlDBComments)
class MysqlDBCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(MongoDBComments)
class MongoDBCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(PostgreSQLDBComments)
class PostgreSQLDBCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(SqliteDBComments)
class SqliteDBCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(OracleDBComments)
class OracleDBCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']


@admin.register(MariaDBComments)
class MariaDBCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']
