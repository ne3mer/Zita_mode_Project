# Generated by Django 4.1.3 on 2022-11-21 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customersquots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='نام مشتری')),
                ('quot', models.TextField(max_length=400, null=True, verbose_name='صحبت مشتری')),
            ],
            options={
                'verbose_name': 'نظر مشتری',
                'verbose_name_plural': 'نظرات مشتریان',
            },
        ),
    ]
