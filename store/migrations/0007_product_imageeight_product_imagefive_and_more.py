# Generated by Django 4.1.2 on 2022-10-06 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_videobanner_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imageEight',
            field=models.ImageField(blank=True, upload_to='products'),
        ),
        migrations.AddField(
            model_name='product',
            name='imageFive',
            field=models.ImageField(blank=True, upload_to='products'),
        ),
        migrations.AddField(
            model_name='product',
            name='imageFour',
            field=models.ImageField(blank=True, upload_to='products'),
        ),
        migrations.AddField(
            model_name='product',
            name='imageNine',
            field=models.ImageField(blank=True, upload_to='products'),
        ),
        migrations.AddField(
            model_name='product',
            name='imageOne',
            field=models.ImageField(blank=True, upload_to='products'),
        ),
        migrations.AddField(
            model_name='product',
            name='imageSeven',
            field=models.ImageField(blank=True, upload_to='products'),
        ),
        migrations.AddField(
            model_name='product',
            name='imageSix',
            field=models.ImageField(blank=True, upload_to='products'),
        ),
        migrations.AddField(
            model_name='product',
            name='imageTen',
            field=models.ImageField(blank=True, upload_to='products'),
        ),
        migrations.AddField(
            model_name='product',
            name='imageThree',
            field=models.ImageField(blank=True, upload_to='products'),
        ),
        migrations.AddField(
            model_name='product',
            name='imageTwo',
            field=models.ImageField(blank=True, upload_to='products'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='image',
            field=models.ImageField(blank=True, upload_to='sub-collections'),
        ),
        migrations.AlterField(
            model_name='videobanner',
            name='url',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
