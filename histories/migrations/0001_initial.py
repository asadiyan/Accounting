# Generated by Django 3.2.5 on 2021-08-17 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('transaction_amount', models.IntegerField()),
                ('transaction_destination', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='destination_account', to='accounts.account')),
                ('transaction_source', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='source_account', to='accounts.account')),
            ],
        ),
    ]