# Generated by Django 5.0.2 on 2024-03-03 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_alter_author_full_name_alter_comment_date_create_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='full_name',
            new_name='fullname',
        ),
    ]
