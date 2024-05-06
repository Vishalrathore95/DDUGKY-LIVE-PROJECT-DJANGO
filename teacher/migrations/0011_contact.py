# Generated by Django 5.0.4 on 2024-05-03 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0010_menuitem_delete_dailymenu_delete_meal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('query', models.TextField()),
                ('language', models.CharField(choices=[('english', 'English'), ('hindi', 'Hindi')], max_length=10)),
            ],
        ),
    ]