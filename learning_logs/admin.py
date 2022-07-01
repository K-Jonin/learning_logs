from django.contrib import admin

# 追加するモデルをインポート
from .models import Topic
from .models import Topic, Entry

# 管理サイトに追加
admin.site.register(Topic)
admin.site.register(Entry)


# Register your models here.
