# Generated by Django 2.2.4 on 2019-09-28 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aidatabase', '0009_auto_20190928_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='ai_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aidatabase.Ai'),
        ),
    ]