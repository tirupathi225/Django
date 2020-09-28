# Generated by Django 2.2.2 on 2019-07-02 05:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cvapp', '0002_auto_20190702_0524'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='score',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
        migrations.CreateModel(
            name='UserCredit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('available_credit', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('used_credit', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('total_earned_credit', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_credit_user', to='cvapp.User')),
            ],
            options={
                'db_table': 'user_credit',
                'ordering': ['-updated_at'],
            },
        ),
    ]
