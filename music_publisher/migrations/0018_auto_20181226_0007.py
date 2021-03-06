# Generated by Django 2.1.4 on 2018-12-25 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_publisher', '0017_auto_20181223_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cwrexport',
            name='nwr_rev',
            field=models.CharField(choices=[('NWR', 'CWR 2.1: New work registration'), ('REV', 'CWR 2.1: Revision of registered work')], db_index=True, default='NWR', max_length=3, verbose_name='CWR version/type'),
        ),
        migrations.AlterUniqueTogether(
            name='writerinwork',
            unique_together={('work', 'writer', 'controlled')},
        ),
    ]
