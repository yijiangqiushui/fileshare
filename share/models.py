from django.db import models
from datetime import datetime

class Upload(models.Model):
    downloaddocount = models.IntegerField(verbose_name=u"访问次数", default=0)
    code = models.CharField(verbose_name=u'code', max_length=8)
    datatime = models.DateTimeField(verbose_name=u'上传时间', default=datetime.now)
    path = models.CharField(verbose_name=u'下载路径', max_length=32)
    name = models.CharField(verbose_name=u'文件名', default='', max_length=32)
    filesize = models.CharField(verbose_name=u'文件大小', max_length=10)
    pcip = models.CharField(verbose_name=u'IP地址', max_length=32, default='')

    class Meta():
        verbose_name = 'download'
        db_table = 'download'

    def __str__(self):
        return self.name
