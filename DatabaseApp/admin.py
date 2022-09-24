from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(MysqlDB)
class MysqlDBAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']


@admin.register(MongoDB)
class MongoDBAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(PostgreSQLDB)
class PostgreSQLDBAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(OracleDB)
class OracleDBAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(SqliteDB)
class SqliteDBAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


@admin.register(MariaDB)
class MariaDBAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    prepopulated_fields = {'slug': ['title']}


# parent
@admin.register(MySqlDBParent)
class MySqlDBParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(MongoDBParent)
class MongoDBParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(PostgreSQLDBParent)
class PostgreSQLDBParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(OracleDBParent)
class OracleDBParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(SqliteDBParent)
class SqliteDBParentAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(MariaDBParent)
class MariaDBParentAdmin(admin.ModelAdmin):
    list_display = ['title']
