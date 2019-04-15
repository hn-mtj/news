# Generated by Django 2.2 on 2019-04-10 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newssite', '0009_auto_20190410_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ManyToManyField(blank=True, null=True, to='newssite.Author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='newssite.Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='count_view',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.ManyToManyField(blank=True, null=True, to='newssite.File'),
        ),
    ]