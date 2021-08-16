# Generated by Django 3.2.5 on 2021-08-16 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customer_identity_code'),
        ('accounts', '0002_alter_account_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.customer'),
        ),
    ]
