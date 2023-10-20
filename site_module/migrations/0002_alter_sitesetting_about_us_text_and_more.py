# Generated by Django 4.2.4 on 2023-09-20 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetting',
            name='about_us_text',
            field=models.TextField(verbose_name='متن درباره ما'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='address',
            field=models.CharField(max_length=200, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='copy_right',
            field=models.TextField(verbose_name='متن کپی رایت'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='fax',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='فکس'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='تلفن'),
        ),
    ]