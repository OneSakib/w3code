from django.db import models
from MainApp.models import TutCommon, Comments,HOST_NAME
from django.urls import reverse_lazy

# Create your models here.


# Database Tut
class MysqlDB(TutCommon):
    class Meta:
        verbose_name_plural = 'MysqlDB'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Database:mysqldetail", kwargs={"slug": self.slug})}'


class MongoDB(TutCommon):
    class Meta:
        verbose_name_plural = 'MongoDB'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Database:mariadbddetail", kwargs={"slug": self.slug})}'


class PostgreSQLDB(TutCommon):
    class Meta:
        verbose_name_plural = 'PostgreSQLDB'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Database:postgresqldetail", kwargs={"slug": self.slug})}'


class OracleDB(TutCommon):
    class Meta:
        verbose_name_plural = 'OracleDB'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Database:oracledetail", kwargs={"slug": self.slug})}'


class SqliteDB(TutCommon):
    class Meta:
        verbose_name_plural = 'SqliteDB'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Database:sqlitedetail", kwargs={"slug": self.slug})}'


class MariaDB(TutCommon):
    class Meta:
        verbose_name_plural = 'MariaDB'
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return f'{HOST_NAME}{reverse_lazy("Database:mariadbddetail", kwargs={"slug": self.slug})}'


# Comments

class MysqlDBComments(Comments):
    post = models.ForeignKey(MysqlDB, on_delete=models.CASCADE, related_name='mysql')

    class Meta:
        verbose_name_plural = 'MysqlDBComments'


class MongoDBComments(Comments):
    post = models.ForeignKey(MongoDB, on_delete=models.CASCADE, related_name='MongoDBComments')

    class Meta:
        verbose_name_plural = 'MongoDBComments'


class PostgreSQLDBComments(Comments):
    post = models.ForeignKey(PostgreSQLDB, on_delete=models.CASCADE, related_name='PostgreSQLDBComments')

    class Meta:
        verbose_name_plural = 'PostgreSQLDBComments'


class SqliteDBComments(Comments):
    post = models.ForeignKey(SqliteDB, on_delete=models.CASCADE, related_name='SqliteDBComments')

    class Meta:
        verbose_name_plural = 'SqliteDBComments'


class OracleDBComments(Comments):
    post = models.ForeignKey(OracleDB, on_delete=models.CASCADE, related_name='OracleDBComments')

    class Meta:
        verbose_name_plural = 'OracleDBComments'


class MariaDBComments(Comments):
    post = models.ForeignKey(MariaDB, on_delete=models.CASCADE, related_name='MariaDBComments')

    class Meta:
        verbose_name_plural = 'MariaDBComments'
