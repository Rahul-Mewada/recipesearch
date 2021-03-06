# Generated by Django 4.0.3 on 2022-03-28 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipies', '0007_alter_image_caption_alter_image_height_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('value', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='rating',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recipies.rating'),
        ),
    ]
