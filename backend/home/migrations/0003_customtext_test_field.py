# Generated by Django 2.2.24 on 2021-12-01 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_customtext_homepage_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='customtext',
            name='test_field',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]