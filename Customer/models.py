from django.db import models


# Create your models here.
class customer(models.Model):
    
    customer_count = models.IntegerField('利用者人数')
    table_number = models.IntegerField('テーブル番号')
    
    def __str__(self):
        
        return self.customer_count
    
class menu_list(models.Model):
    
    name = models.CharField('メニュー名', max_length=100)
    count = models.IntegerField('価格')
    
    def __str__(self):
        
        return self.name

    
