# Generated by Django 5.0 on 2024-04-28 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archcode', '0002_alter_image_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('senha', models.CharField(max_length=100)),
            ],
        ),
    ]
