# Generated by Django 2.1.4 on 2019-04-19 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plantjournal', '0003_auto_20190418_2154'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plant',
            options={'ordering': ['plant_name', 'plant_number', 'plant_nickname']},
        ),
        migrations.AlterField(
            model_name='plant',
            name='fertilizer',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='plants', to='plantjournal.Fertilizer'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='flower',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='plants', to='plantjournal.Flower'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='humidity',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='plants', to='plantjournal.Humidity'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='light',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='plants', to='plantjournal.Light'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='location',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='plants', to='plantjournal.Location'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='soil',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='plants', to='plantjournal.Soil'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='toxicity',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='plants', to='plantjournal.Toxicity'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='water',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='plants', to='plantjournal.Water'),
        ),
        migrations.AlterUniqueTogether(
            name='plant',
            unique_together={('plant_name', 'plant_number', 'plant_nickname')},
        ),
    ]
