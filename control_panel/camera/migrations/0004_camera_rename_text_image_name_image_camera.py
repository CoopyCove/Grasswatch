# Generated by Django 4.0.3 on 2022-03-28 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0003_image_delete_simple'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='image',
            old_name='text',
            new_name='name',
        ),
        migrations.AddField(
            model_name='image',
            name='camera',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='camera.camera'),
        ),
    ]
