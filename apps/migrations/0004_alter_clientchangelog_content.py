# Generated by Django 4.1.3 on 2022-12-15 08:22

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_clientchangelog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientchangelog',
            name='content',
            field=mdeditor.fields.MDTextField(blank=True, null=True),
        ),
    ]
