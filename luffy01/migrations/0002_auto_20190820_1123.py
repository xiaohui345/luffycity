# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-08-20 03:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('luffy01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tokeninfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tokens', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=64)),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='tokeninfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='luffy01.Userinfo'),
        ),
    ]