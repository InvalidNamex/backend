# Generated by Django 4.1.1 on 2022-09-24 16:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_videobanner_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brandbanner',
            name='product',
        ),
        migrations.AddField(
            model_name='brandbanner',
            name='brand',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.PROTECT, to='store.brand'),
            preserve_default=False,
        ),
    ]
