# Generated by Django 3.2.7 on 2021-10-17 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0001_initial'),
        ('CustomerProfile', '0001_initial'),
        ('Accounts', '0001_initial'),
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Custorders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('mobile_no', models.BigIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('price', models.IntegerField()),
                ('items', models.IntegerField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='CustomerProfile.address')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.customer')),
                ('grocery', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Seller.grocery')),
                ('laptop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Seller.laptop')),
                ('mobile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Seller.mobile')),
            ],
        ),
    ]
