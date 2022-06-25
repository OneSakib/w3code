from django.contrib.sitemaps import Sitemap
from .models import *


class CommonSitemap(Sitemap):
    change_freq = "weekly"
    priority = 0.7

    def lastmod(self, obj):
        return obj.timestamp


class MysqlDB_Sitemap(CommonSitemap):
    def items(self):
        return MysqlDB.objects.all()


class MongoDB_Sitemap(CommonSitemap):
    def items(self):
        return MongoDB.objects.all()


class PostgreSQLDB_Sitemap(CommonSitemap):
    def items(self):
        return PostgreSQLDB.objects.all()


class OracleDB_Sitemap(CommonSitemap):
    def items(self):
        return OracleDB.objects.all()


class SqliteDB_Sitemap(CommonSitemap):
    def items(self):
        return SqliteDB.objects.all()


class MariaDB_Sitemap(CommonSitemap):
    def items(self):
        return MariaDB.objects.all()


D_sitemap = {
    'MySqlDB_Sitemap': MysqlDB_Sitemap,
    'MongoDB_Sitemap': MongoDB_Sitemap,
    'PostgreSQLDB_Sitemap': PostgreSQLDB_Sitemap,
    'OracleDB_Sitemap': OracleDB_Sitemap,
    'SqliteDB_Sitemap': SqliteDB_Sitemap,
    'MariaDB_Sitemap': MariaDB_Sitemap
}
