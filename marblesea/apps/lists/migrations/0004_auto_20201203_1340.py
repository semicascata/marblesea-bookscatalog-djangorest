# Generated by Django 3.1.3 on 2020-12-03 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0003_book_publisher_user'),
        ('lists', '0003_auto_20201203_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='book',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='book_list', to='books.book'),
        ),
        migrations.AlterField(
            model_name='list',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_books', to=settings.AUTH_USER_MODEL),
        ),
    ]
