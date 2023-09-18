# Generated by Django 4.2.5 on 2023-09-18 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('image_handling', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetectionResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detected_objects', models.TextField()),
                ('image', models.ImageField(upload_to='detection_results/')),
                ('detection_date', models.DateTimeField(auto_now_add=True)),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image_handling.submittedformdata')),
            ],
        ),
    ]