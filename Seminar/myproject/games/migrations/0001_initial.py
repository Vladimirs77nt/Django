# Generated by Django 5.0.2 on 2024-02-14 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Heads_or_tails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side', models.CharField(max_length=5)),
                ('datetimestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
