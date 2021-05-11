from django.conf import settings
from django.db import models
from django.utils import timezone

# クラスはオブジェクトを定義している。
class Post(models.Model):
    '''
    models.CharField: 文字数が制限されたテキストを定義するフィールド
    models.TextField: 制限なしの長いテキスト用フィールド
    models.DateTimeField: 日付と時間のフィールド
    models.ForeignKey: 他のモデルへのリンク
    '''
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # メソッド
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    # メソッド
    def __str__(self):
        return self.title