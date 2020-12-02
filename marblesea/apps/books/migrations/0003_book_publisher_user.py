# Generated by Django 3.1.3 on 2020-12-02 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0002_book_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publisher_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='publisher_user', to='auth.user'),
            preserve_default=False,
        ),
    ]