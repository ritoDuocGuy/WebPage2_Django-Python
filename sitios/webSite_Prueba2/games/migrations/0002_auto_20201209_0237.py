# Generated by Django 2.2.16 on 2020-12-09 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['created'], 'verbose_name': 'Juego', 'verbose_name_plural': 'Juegos'},
        ),
        migrations.RenameField(
            model_name='project',
            old_name='short_description',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='long_description',
        ),
    ]