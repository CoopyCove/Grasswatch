# Generated by Django 3.2.5 on 2022-05-05 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0005_merge_20220504_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='notification_interval',
            field=models.CharField(choices=[('Immediately', 'immediate'), ('Daily', 'daily'), ('Weekly', 'weekly')], default='weekly', max_length=11),
        ),
    ]