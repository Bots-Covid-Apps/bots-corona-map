# Generated by Django 3.0.5 on 2020-04-14 20:28

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('gaborone', '0003_patient_plot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='condition',
        ),
        migrations.AddField(
            model_name='patient',
            name='conditions',
            field=models.ManyToManyField(help_text='Patients Pre-exsisting Condition', to='gaborone.Condition'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(default=0, help_text='Age of Person'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='has_had_contact',
            field=models.BooleanField(help_text='Has the patient had contact with anyone with the virus'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='has_tested',
            field=models.BooleanField(blank=True, help_text='Has the patient been tested and what is the result', null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='has_travelled',
            field=models.BooleanField(help_text='Has the patient travled to an affected area'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='plot',
            field=models.IntegerField(blank=True, null=True, verbose_name='Plot Number'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='symptoms',
            field=models.ManyToManyField(help_text='Current Symptoms', to='gaborone.Symptom'),
        ),
    ]
