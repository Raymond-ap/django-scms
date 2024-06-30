# Generated by Django 5.0.1 on 2024-06-30 20:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academic', '0002_initial'),
        ('finance', '0001_initial'),
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='paid_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.accountant'),
        ),
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='payment',
            name='paid_for',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='finance.paymentallocation'),
        ),
        migrations.AddField(
            model_name='receipt',
            name='received_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.accountant'),
        ),
        migrations.AddField(
            model_name='receipt',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='academic.student'),
        ),
        migrations.AddField(
            model_name='receipt',
            name='paid_for',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='finance.receiptallocation'),
        ),
    ]
