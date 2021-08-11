# Generated by Django 3.2.5 on 2021-08-11 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('identity_code', models.IntegerField()),
            ],
        ),
    ]
