# Generated by Django 3.2.3 on 2021-11-22 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_id', models.IntegerField()),
                ('genre_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ott',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idx', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('eng_title', models.CharField(max_length=100)),
                ('overview', models.TextField()),
                ('released_date', models.DateField()),
                ('poster_path', models.TextField()),
                ('popularity', models.IntegerField()),
                ('vote_average', models.IntegerField()),
                ('vote_cnt', models.IntegerField()),
                ('movie_genre', models.ManyToManyField(blank=True, null=True, related_name='movie_genre', to='movies.Genre')),
                ('movie_ott', models.ManyToManyField(blank=True, null=True, related_name='movie_ott', to='movies.Ott')),
            ],
        ),
    ]
