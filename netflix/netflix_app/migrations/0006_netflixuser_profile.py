# Generated by Django 5.0.3 on 2024-03-14 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netflix_app', '0005_netflixprofile_remove_netflixuser_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='netflixuser',
            name='profile',
            field=models.ManyToManyField(to='netflix_app.netflixprofile', verbose_name='Diğer Profiller'),
        ),
    ]
