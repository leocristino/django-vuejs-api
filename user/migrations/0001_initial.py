# Generated by Django 2.1.5 on 2019-01-19 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'FEMALE')], default='', max_length=15)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]