# Generated by Django 5.0.2 on 2024-02-29 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
