# Generated by Django 2.2 on 2019-04-23 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_auto_20190418_0220'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(blank=True, help_text='Task image', upload_to='images/%Y_%m_%d', verbose_name='Image'),
        ),
    ]
