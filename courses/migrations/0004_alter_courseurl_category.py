# Generated by Django 3.2.8 on 2021-11-02 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20211102_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseurl',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.category'),
        ),
    ]
