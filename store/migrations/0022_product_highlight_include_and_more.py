# Generated by Django 4.1.3 on 2023-02-09 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_product_banner_include'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='highlight_include',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='highlight_section_name',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='highlight_section_product',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
