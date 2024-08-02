# Generated by Django 4.2.2 on 2023-10-28 08:35

from django.db import migrations, models
import django.db.models.deletion
import providers.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_id', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('about', models.TextField(blank=True, max_length=500)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='describe', to='providers.category')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('about', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Providers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider_id', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(blank=True, upload_to=providers.models.path_and_name, verbose_name='Provider Profile')),
                ('location', models.CharField(blank=True, max_length=30)),
                ('clients', models.IntegerField(default=0)),
                ('experience', models.IntegerField(default=0)),
                ('age', models.IntegerField(default=0)),
                ('video', models.FileField(blank=True, upload_to=providers.models.save_video_files, verbose_name='proof')),
                ('picture', models.ImageField(blank=True, upload_to=providers.models.save_image_file, verbose_name='Pictures')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.category')),
                ('description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pro', to='providers.description')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.service')),
            ],
        ),
        migrations.AddField(
            model_name='description',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.service'),
        ),
        migrations.AddField(
            model_name='category',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat', to='providers.service'),
        ),
    ]
