# Generated by Django 4.0.5 on 2022-07-02 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JavaScriptApp', '0003_alter_angularjs_options_alter_expressjs_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expressjscomments',
            name='comments_ptr',
        ),
        migrations.RemoveField(
            model_name='expressjscomments',
            name='post',
        ),
        migrations.RemoveField(
            model_name='jquerycomments',
            name='comments_ptr',
        ),
        migrations.RemoveField(
            model_name='jquerycomments',
            name='post',
        ),
        migrations.RemoveField(
            model_name='nodejscomments',
            name='comments_ptr',
        ),
        migrations.RemoveField(
            model_name='nodejscomments',
            name='post',
        ),
        migrations.RemoveField(
            model_name='reactjscomments',
            name='comments_ptr',
        ),
        migrations.RemoveField(
            model_name='reactjscomments',
            name='post',
        ),
        migrations.RemoveField(
            model_name='typescriptscomments',
            name='comments_ptr',
        ),
        migrations.RemoveField(
            model_name='typescriptscomments',
            name='post',
        ),
        migrations.RemoveField(
            model_name='vuejscomments',
            name='comments_ptr',
        ),
        migrations.RemoveField(
            model_name='vuejscomments',
            name='post',
        ),
        migrations.DeleteModel(
            name='AngularjsComments',
        ),
        migrations.DeleteModel(
            name='ExpressjsComments',
        ),
        migrations.DeleteModel(
            name='JqueryComments',
        ),
        migrations.DeleteModel(
            name='NodejsComments',
        ),
        migrations.DeleteModel(
            name='ReactjsComments',
        ),
        migrations.DeleteModel(
            name='TypeScriptsComments',
        ),
        migrations.DeleteModel(
            name='VUEjsComments',
        ),
    ]
