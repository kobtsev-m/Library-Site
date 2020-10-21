# Generated by Django 2.2.6 on 2020-10-19 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20201020_0452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='library/media/books/'),
        ),
        migrations.AlterField(
            model_name='contentimage',
            name='url',
            field=models.ImageField(blank=True, null=True, upload_to='library/media/content/'),
        ),
    ]