# Generated by Django 3.1.1 on 2020-10-03 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rope', '0003_delete_buffalo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cow',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coew', to='rope.milk'),
        ),
    ]
