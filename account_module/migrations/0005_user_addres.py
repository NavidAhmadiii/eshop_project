# Generated by Django 4.2.4 on 2023-10-12 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0004_alter_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='addres',
            field=models.TextField(blank=True, null=True, verbose_name='آدرس'),
        ),
    ]