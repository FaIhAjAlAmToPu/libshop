# Generated by Django 5.2 on 2025-04-17 18:27

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contents', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('libraries', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='StoreWishlist',
            fields=[
                ('wishlist_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='notifications.wishlist')),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('notifications.wishlist',),
        ),
        migrations.CreateModel(
            name='StoryWishlist',
            fields=[
                ('wishlist_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='notifications.wishlist')),
                ('plot', models.TextField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('notifications.wishlist',),
        ),
        migrations.CreateModel(
            name='BookWishlist',
            fields=[
                ('wishlist_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='notifications.wishlist')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.book')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraries.store')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('notifications.wishlist',),
        ),
        migrations.CreateModel(
            name='WishBookByAuthor',
            fields=[
                ('wishlist_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='notifications.wishlist')),
                ('genre', models.CharField(max_length=30)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.author')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('notifications.wishlist',),
        ),
        migrations.CreateModel(
            name='WishStoryByAuthor',
            fields=[
                ('wishlist_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='notifications.wishlist')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('notifications.wishlist',),
        ),
    ]
