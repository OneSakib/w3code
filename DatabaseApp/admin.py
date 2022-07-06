from django.contrib import admin
from .models import *
from MainApp.admin import CommonAdmin

# Register your models here.


class MysqlDBAdmin(CommonAdmin):
    model = MysqlDB


class MongoDBAdmin(CommonAdmin):
    model = MongoDB


class PostgreSQLDBAdmin(CommonAdmin):
    model = PostgreSQLDB


class OracleDBAdmin(CommonAdmin):
    model = OracleDB


class SqliteDBAdmin(CommonAdmin):
    model = SqliteDB


class MariaDBAdmin(CommonAdmin):
    model = MariaDB


# parent
@admin.register(MySqlDBParent)
class MySqlDBParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (MysqlDBAdmin,)


@admin.register(MongoDBParent)
class MongoDBParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (MongoDBAdmin,)


@admin.register(PostgreSQLDBParent)
class PostgreSQLDBParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (PostgreSQLDBAdmin,)


@admin.register(OracleDBParent)
class OracleDBParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (OracleDBAdmin,)


@admin.register(SqliteDBParent)
class SqliteDBParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (SqliteDBAdmin,)


@admin.register(MariaDBParent)
class MariaDBParentAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = (MariaDBAdmin,)
