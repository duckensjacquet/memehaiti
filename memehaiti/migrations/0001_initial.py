# Generated by Django 4.2.3 on 2023-07-19 20:12

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Meme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file', cloudinary.models.CloudinaryField(max_length=255, verbose_name='file')),
                ('format', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ManyToManyField(to='memehaiti.category')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('meme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memehaiti.meme')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memehaiti.user')),
            ],
        ),
        migrations.AddField(
            model_name='meme',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memehaiti.user'),
        ),
        migrations.AddField(
            model_name='meme',
            name='keywords',
            field=models.ManyToManyField(to='memehaiti.keyword'),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('meme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memehaiti.meme')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memehaiti.user')),
            ],
        ),
        migrations.CreateModel(
            name='GeneratedMeme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', cloudinary.models.CloudinaryField(max_length=255, verbose_name='file')),
                ('format', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memehaiti.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('meme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memehaiti.meme')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memehaiti.user')),
            ],
        ),
    ]
