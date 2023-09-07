# Generated by Django 4.2.4 on 2023-08-11 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_productmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='wishmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('pid', models.IntegerField()),
                ('pname', models.CharField(max_length=50)),
                ('pcid', models.CharField(max_length=50)),
                ('prode', models.CharField(max_length=500)),
                ('pimage', models.FileField(upload_to='')),
                ('price', models.IntegerField()),
            ],
        ),
    ]
