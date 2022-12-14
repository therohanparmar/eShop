# Generated by Django 4.0.6 on 2022-08-07 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=50)),
                ('sub_category', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('desc', models.CharField(max_length=300)),
                ('pub_date', models.DateField()),
                ('imege', models.ImageField(upload_to='shop/images')),
            ],
        ),
    ]
