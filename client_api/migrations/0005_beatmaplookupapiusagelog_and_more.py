# Generated by Django 4.1.3 on 2023-01-23 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_api', '0004_beatmapsetlookupapiusagelog'),
    ]

    operations = [
        migrations.CreateModel(
            name='BeatmapLookupAPIUsageLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('beatmapset_id', models.IntegerField()),
                ('success', models.BooleanField(default=False)),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.RenameField(
            model_name='beatmapsetlookupapiusagelog',
            old_name='beatmapset_id',
            new_name='lookup_id',
        ),
        migrations.AddField(
            model_name='beatmapsetlookupapiusagelog',
            name='lookup_type',
            field=models.CharField(default='', max_length=100),
        ),
    ]
