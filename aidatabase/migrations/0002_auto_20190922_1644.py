# Generated by Django 2.2.4 on 2019-09-22 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aidatabase', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ai',
            name='alien_technology',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='consciousness',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='creator_rel',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='difference',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='emotional',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='explicit_mention',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='female_creator',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='free_will',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='harmed_humans',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='harms_creator',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='integration',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='intelligence',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='intimacy',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='learning',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='manifestation',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='more_control',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='on_purpose',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='owner_rel',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='physical',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='rebellious',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='servant',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='society_pos',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='technical',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='told_by',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='warrior',
        ),
        migrations.RemoveField(
            model_name='ai',
            name='world_domination',
        ),
        migrations.AddField(
            model_name='author',
            name='firstname',
            field=models.CharField(default='firstname', max_length=30, verbose_name='firstname'),
        ),
        migrations.AddField(
            model_name='author',
            name='lastname',
            field=models.CharField(default='lastname', max_length=30, verbose_name='lastname'),
        ),
        migrations.AlterField(
            model_name='ai',
            name='name',
            field=models.CharField(help_text='real name', max_length=20, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=30, verbose_name='lastname-firstname(s)'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('1', 'X'), ('2', 'XX'), ('3', 'XXX'), ('4', 'XXXX'), ('5', 'XXXXX')], max_length=1)),
                ('manifestation', models.TextField()),
                ('physical', models.CharField(choices=[('1', 'X'), ('2', 'XX'), ('3', 'XXX'), ('4', 'XXXX'), ('5', 'XXXXX')], max_length=1)),
                ('difference', models.TextField()),
                ('technical', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=1)),
                ('consciousness', models.CharField(choices=[('1', 'X'), ('2', 'XX'), ('3', 'XXX'), ('4', 'XXXX'), ('5', 'XXXXX')], max_length=1)),
                ('intelligence', models.CharField(choices=[('1', 'X'), ('2', 'XX'), ('3', 'XXX'), ('4', 'XXXX')], max_length=1)),
                ('free_will', models.BooleanField()),
                ('learning', models.BooleanField()),
                ('emotional', models.BooleanField()),
                ('integration', models.CharField(choices=[('1', 'X'), ('2', 'XX'), ('3', 'XXX'), ('4', 'XXXX')], max_length=1)),
                ('on_purpose', models.BooleanField()),
                ('creator_rel', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=1)),
                ('owner_rel', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=1)),
                ('female_creator', models.BooleanField()),
                ('society_pos', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=1)),
                ('subject', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=1)),
                ('servant', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=1)),
                ('intimacy', models.CharField(choices=[('1', 'X'), ('2', 'XX'), ('3', 'XXX'), ('4', 'XXXX')], max_length=1)),
                ('told_by', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=1)),
                ('quantity', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=1)),
                ('warrior', models.BooleanField()),
                ('rebellious', models.BooleanField()),
                ('harmed_humans', models.BooleanField()),
                ('harms_creator', models.BooleanField()),
                ('more_control', models.BooleanField()),
                ('world_domination', models.BooleanField()),
                ('alien_technology', models.BooleanField()),
                ('explicit_mention', models.BooleanField()),
                ('registered_on', models.DateTimeField(blank=True, null=True)),
                ('ai_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aidatabase.Ai')),
                ('registered_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
