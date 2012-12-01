# -*- coding: utf-8 -*-
from django.db import models
import datetime

class FinanceItem(models.Model):
    def __unicode__(self):
        return self.itemname
    
    itemname = models.CharField("消费条目",max_length=128)
    costs = models.DecimalField("消费金额",max_digits=9,decimal_places=2)
    detailinfo = models.TextField("详细描述",max_length=4000,blank=True,null=True)
    cost_date = models.DateTimeField("消费日期", default=datetime.datetime.now)
    