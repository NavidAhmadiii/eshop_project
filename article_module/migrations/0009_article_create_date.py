# Generated by Django 4.2.4 on 2023-10-04 10:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0008_alter_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2023, 10, 4), verbose_name='تاریخ ثبت'),
            preserve_default=False,
        ),
    ]
