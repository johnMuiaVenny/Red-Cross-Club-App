# Generated by Django 3.2.5 on 2021-07-03 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nature_club', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('Images', models.FileField(upload_to='events')),
            ],
        ),
    ]
