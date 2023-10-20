# Generated by Django 4.2.4 on 2023-10-09 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0010_articlecomment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlecomment',
            options={'verbose_name': 'نظر مقاله', 'verbose_name_plural': 'نظرات مقالات'},
        ),
        migrations.AlterField(
            model_name='articlecomment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='article_module.articlecomment', verbose_name='والد'),
        ),
    ]