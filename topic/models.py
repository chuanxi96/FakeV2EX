from datetime import datetime
from django.db import models
from user.models import UserProfile
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


class TopicCategory(models.Model):
    """
    Topic类别
    """
    CATEGORY_TYPE = (
        (1, "tab"),
        (2, "go"),
    )

    name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
    code = models.CharField(default="", max_length=30, verbose_name="类别code", help_text="类别code")
    icon = models.CharField(null=True, blank=True, max_length=50, verbose_name="图标", help_text="图标")
    desc = models.TextField(null=True, blank=True, verbose_name="类别描述", help_text="类别描述")
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别", help_text="父目录",
                                        related_name="sub_cat", on_delete=models.CASCADE)
    is_hot = models.BooleanField(default=False, verbose_name="是否最热", help_text="是否最热")
    avatar = models.CharField(max_length=50, null=True, blank=True, default="/static/img/default-avatar.png",
                              verbose_name="头像")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "Tips类别"
        verbose_name_plural = verbose_name
        unique_together = ('code', 'category_type',)

    def __str__(self):
        return self.name


class Topic(models.Model):
    """
    Topic
    """
    category = models.ForeignKey(TopicCategory, verbose_name="Go分类", on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name="Topic作者", on_delete=models.CASCADE)
    topic_sn = models.CharField(max_length=50, default="", unique=True, verbose_name="Topic唯一sn")
    click_num = models.IntegerField(default=0, verbose_name="Topic点击数")
    title = models.TextField(max_length=120, verbose_name="Topic title")
    content = models.TextField(max_length=20000, verbose_name="Topic title")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class TopicVote(models.Model):
    """
    Topic Vote
    """
    user = models.ForeignKey(User, verbose_name="用户", on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, verbose_name="Topic", on_delete=models.CASCADE)
    like = models.BooleanField(verbose_name="是否喜欢此贴")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user

    def count_like(self, topic_obj):
        return TopicVote.objects.filter(like=True, topic=topic_obj).count()

    def count_dislike(self, topic_obj):
        return TopicVote.objects.filter(like=False, topic=topic_obj).count()
