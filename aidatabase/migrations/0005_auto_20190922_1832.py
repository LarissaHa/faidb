# Generated by Django 2.2.4 on 2019-09-22 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aidatabase', '0004_auto_20190922_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author_id',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='aidatabase.Author'),
        ),
        migrations.AlterField(
            model_name='review',
            name='ai_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aidatabase.Ai'),
        ),
    ]