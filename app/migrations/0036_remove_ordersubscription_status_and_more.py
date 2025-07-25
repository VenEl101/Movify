# Generated by Django 5.2 on 2025-05-22 09:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_alter_payment_payment_method_alter_user_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordersubscription',
            name='status',
        ),
        migrations.RemoveField(
            model_name='ordersubscription',
            name='subscription',
        ),
        migrations.CreateModel(
            name='OrderSubscriptionItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('PENDING', 'pending'), ('FAILED', 'failed'), ('COMPLETED', 'completed')], db_default='PENDING', max_length=25)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='app.ordersubscription')),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status', to='app.subscriptionitems')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='PaymentSubscription',
        ),
    ]
