# Generated by Django 3.0.6 on 2020-07-31 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0007_auto_20200731_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='calorie',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='carbonhydrate',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='name',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='barcode',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='carbohydrate',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='foodtype',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='kcal',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='one_supply',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='product_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='region',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='total_content',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='cholesterol',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='fat',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='protein',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='sodium',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]