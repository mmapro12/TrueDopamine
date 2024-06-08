from django.db import models

# Create your models here.

CATEGORY_CHOCIES = [
    ('islamiyat', 'إسلاميات'),
    ('self-up', 'تطوير الذات'),
    ('sport', 'رياضة'),
    ('programming', 'برمجة'),
    ('montage', 'منتاج'),
    ('random', 'منوع'),
    ('language', 'تعلم لغات'),
    ('ai', 'الذكاء الإصطناعي'),
    
]

class Card(models.Model):
    name = models.CharField(max_length=200)
    # youtube_img = models.URLField(max_length=600)
    youtube_url = models.URLField(max_length=600)

    category = models.CharField(max_length=30, choices=CATEGORY_CHOCIES)

    def __str__(self):
        return self.name

