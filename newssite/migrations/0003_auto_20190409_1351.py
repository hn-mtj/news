# Generated by Django 2.2 on 2019-04-09 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newssite', '0002_auto_20190409_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('birth_day', models.DateTimeField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('file_name', models.CharField(max_length=255)),
                ('caption', models.CharField(max_length=255)),
                ('summary', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=5)),
                ('size', models.IntegerField()),
                ('status', models.IntegerField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='language',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='newssite.Language'),
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='newssite.Location'),
        ),
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='newssite.Post')),
                ('tag', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='newssite.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='PostFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='newssite.Post')),
                ('tag', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='newssite.File')),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='newssite.Category')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='newssite.Post')),
            ],
        ),
        migrations.CreateModel(
            name='PostAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='newssite.Post')),
                ('tag', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='newssite.Author')),
            ],
        ),
    ]
