# Generated by Django 3.1.6 on 2021-02-09 05:48

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
                ('name', models.CharField(max_length=264, unique=True)),
                ('password', models.CharField(max_length=10)),
                ('confirm_password', models.CharField(max_length=10)),
            ],
        ),
    ]
