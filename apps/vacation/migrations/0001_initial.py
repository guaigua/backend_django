# Generated by Django 4.1.7 on 2023-04-12 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0003_alter_client_company_alter_client_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days_total', models.IntegerField()),
                ('days_used', models.IntegerField(default=0)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
        ),
    ]