# Generated by Django 3.2 on 2021-04-30 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.CharField(default='No data', max_length=10000),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(default='No data', max_length=10000),
        ),
        migrations.AddField(
            model_name='product',
            name='link',
            field=models.CharField(default='No data', max_length=10000),
        ),
    ]
