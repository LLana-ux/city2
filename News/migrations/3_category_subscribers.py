from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0002_alter_comment_user_alter_post_author"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="subscribers",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="categories",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]