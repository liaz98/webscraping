# Generated by Django 3.2.8 on 2021-11-03 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20211103_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseurl',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courseurl', to='courses.category'),
        ),
    ]