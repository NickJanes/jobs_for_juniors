# Generated by Django 4.2.6 on 2023-12-12 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posting', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='application',
            name='posting_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posting.posting'),
        ),
        migrations.AddField(
            model_name='application',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='postingtag',
            constraint=models.UniqueConstraint(fields=('posting', 'tag'), name='unique_tag_post'),
        ),
    ]
