# Generated by Django 3.1.3 on 2020-12-18 20:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0002_note_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
