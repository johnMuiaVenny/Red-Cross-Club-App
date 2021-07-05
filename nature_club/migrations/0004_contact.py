# Generated by Django 3.2.5 on 2021-07-04 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nature_club', '0003_leadership'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', models.CharField(max_length=100)),
                ('Subject', models.CharField(max_length=100)),
                ('Message', models.TextField()),
            ],
        ),
    ]
