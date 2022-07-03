from django.db import models
from MainApp.models import TutCommon, Comments,HOST_NAME
from django.urls import reverse_lazy

# Create your models here.


# Database Tut
class MysqlDB(TutCommon):
    class Meta:
        verbose_name_plural = 'MysqlDB'

    def get_absolute_url(self):
        return f'{reverse_lazy("Database:mysqldetail", kwargs={"slug": self.slug})}'


class MongoDB(TutCommon):
    class Meta:
        verbose_name_plural = 'MongoDB'


    def get_absolute_url(self):
        return f'{reverse_lazy("Database:mariadbddetail", kwargs={"slug": self.slug})}'


class PostgreSQLDB(TutCommon):
    class Meta:
        verbose_name_plural = 'PostgreSQLDB'


    def get_absolute_url(self):
        return f'{reverse_lazy("Database:postgresqldetail", kwargs={"slug": self.slug})}'


class OracleDB(TutCommon):
    class Meta:
        verbose_name_plural = 'OracleDB'


    def get_absolute_url(self):
        return f'{reverse_lazy("Database:oracledetail", kwargs={"slug": self.slug})}'


class SqliteDB(TutCommon):
    class Meta:
        verbose_name_plural = 'SqliteDB'

    def get_absolute_url(self):
        return f'{reverse_lazy("Database:sqlitedetail", kwargs={"slug": self.slug})}'


class MariaDB(TutCommon):
    class Meta:
        verbose_name_plural = 'MariaDB'

    def get_absolute_url(self):
        return f'{reverse_lazy("Database:mariadbddetail", kwargs={"slug": self.slug})}'

