# Generated by Django 3.2.6 on 2021-08-04 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default=1, upload_to='jobs', verbose_name='images'),
            preserve_default=False,
        ),
    ]