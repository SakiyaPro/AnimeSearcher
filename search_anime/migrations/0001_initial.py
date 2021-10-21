# Generated by Django 3.2.8 on 2021-10-21 07:10

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(null=True, verbose_name='タイトル')),
                ('star', models.FloatField(null=True, verbose_name='評価')),
                ('story', models.TextField(null=True, verbose_name='あらすじ')),
                ('img_path', models.TextField(null=True, verbose_name='画像パス')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name_plural': 'AnimeData',
                'db_table': 'anime_db',
            },
        ),
    ]
