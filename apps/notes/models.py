from django.db import models


# Create your models here.
class Notes(models.Model):
    time = models.DateTimeField(auto_now_add=True, verbose_name='记录时间')
    title = models.CharField(max_length=255, verbose_name='标题', null=True, blank=True)
    info = models.TextField(verbose_name='内容', null=True, blank=True)
    user = models.ForeignKey('system.UserModel', on_delete=models.DO_NOTHING, verbose_name='用户', null=True, blank=True)
    is_delete = models.BooleanField(default=False, null=True, blank=True, verbose_name='是否删除')

    class Meta:
        db_table = 'notes'
        verbose_name = '笔记表'
