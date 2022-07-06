from django.db import models
from MainApp.models import TutCommon, TutCommonParent, LikeCommon
from django.urls import reverse_lazy


# Create your models here.


# Database Tut
# Parent
class MySqlDBParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'MySqlDB Parent'

    def get_child(self):
        return MysqlDB.objects.all()


class MongoDBParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'MongoDB Parent'

    def get_child(self):
        return MongoDB.objects.all()


class PostgreSQLDBParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'PostgreSQLDB Parent'

    def get_child(self):
        return PostgreSQLDB.objects.all()


class OracleDBParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'OracleDB Parent'

    def get_child(self):
        return OracleDB.objects.all()


class SqliteDBParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'SqliteDB Parent'

    def get_child(self):
        return SqliteDB.objects.all()


class MariaDBParent(TutCommonParent):
    class Meta:
        verbose_name_plural = 'MariaDB Parent'

    def get_child(self):
        return MariaDB.objects.all()


# Child
class MysqlDB(TutCommon):
    parent = models.ForeignKey(MySqlDBParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'MysqlDB'

    def get_absolute_url(self):
        return f'{reverse_lazy("Database:mysqldetail", kwargs={"slug": self.slug})}'


class MongoDB(TutCommon):
    parent = models.ForeignKey(MongoDBParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'MongoDB'

    def get_absolute_url(self):
        return f'{reverse_lazy("Database:mariadbddetail", kwargs={"slug": self.slug})}'


class PostgreSQLDB(TutCommon):
    parent = models.ForeignKey(PostgreSQLDBParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'PostgreSQLDB'

    def get_absolute_url(self):
        return f'{reverse_lazy("Database:postgresqldetail", kwargs={"slug": self.slug})}'


class OracleDB(TutCommon):
    parent = models.ForeignKey(OracleDBParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'OracleDB'

    def get_absolute_url(self):
        return f'{reverse_lazy("Database:oracledetail", kwargs={"slug": self.slug})}'


class SqliteDB(TutCommon):
    parent = models.ForeignKey(SqliteDBParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'SqliteDB'

    def get_absolute_url(self):
        return f'{reverse_lazy("Database:sqlitedetail", kwargs={"slug": self.slug})}'


class MariaDB(TutCommon):
    parent = models.ForeignKey(MariaDBParent, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'MariaDB'

    def get_absolute_url(self):
        return f'{reverse_lazy("Database:mariadbddetail", kwargs={"slug": self.slug})}'


# Like Counter
class MysqlDBLike(LikeCommon):
    post = models.ForeignKey(MysqlDB, on_delete=models.CASCADE)


class MongoDBLike(LikeCommon):
    post = models.ForeignKey(MongoDB, on_delete=models.CASCADE)


class PostgreSQLDBLike(LikeCommon):
    post = models.ForeignKey(PostgreSQLDB, on_delete=models.CASCADE)


class OracleDBLike(LikeCommon):
    post = models.ForeignKey(OracleDB, on_delete=models.CASCADE)


class SqliteDBLike(LikeCommon):
    post = models.ForeignKey(SqliteDB, on_delete=models.CASCADE)


class MariaDBLike(LikeCommon):
    post = models.ForeignKey(MariaDB, on_delete=models.CASCADE)
