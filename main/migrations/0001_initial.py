# Generated by Django 3.2 on 2021-04-18 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('quantity', models.IntegerField(default=0, null=True)),
                ('startdate', models.DateTimeField(null=True)),
                ('duedate', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed'), ('Awarded', 'Awarded')], max_length=10, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quotamount', models.FloatField(null=True)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed'), ('Awarded', 'Awarded')], max_length=50, null=True)),
                ('tender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.tender')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
