# Generated by Django 5.0.6 on 2024-06-08 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_cardchoices_alter_card_youtube_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='category',
            field=models.CharField(choices=[('islamiyat', 'إسلاميات'), ('self-up', 'تطوير الذات'), ('sport', 'رياضة'), ('programming', 'برمجة'), ('montage', 'منتاج'), ('random', 'منوع'), ('language', 'تعلم لغات'), ('ai', 'الذكاء الإصطناعي')], max_length=30),
        ),
        migrations.RemoveField(
            model_name='card',
            name='youtube_img',
        ),
        migrations.DeleteModel(
            name='CardChoices',
        ),
    ]
