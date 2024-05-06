# Generated by Django 5.0.4 on 2024-05-02 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0006_delete_tsc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tsc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('profile_image', models.ImageField(upload_to='tsc/profiles/')),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('year', models.IntegerField()),
                ('batch_name', models.CharField(max_length=100)),
            ],
        ),
    ]