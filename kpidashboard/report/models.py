from django.db import models
# Create your models here.

class Ft_all(models.Model):
    product_group = models.CharField(max_length=20)
    MarketPlace_Id = models.IntegerField()
    week_ending = models.DateField()
    total_ft_p = models.FloatField()
    ft_retail_p = models.FloatField()
    ft_fba_p = models.FloatField()
    ctrl_p = models.FloatField()
    x3p_ctrl_p = models.FloatField()
    x3p_non_ctrl_p = models.FloatField()
    nofr_p = models.FloatField()      
    total_ft = models.IntegerField()
    ft_retail =  models.IntegerField()
    ft_fba =  models.IntegerField()
    ctrl =  models.IntegerField()
    x3p_ctrl =  models.IntegerField()
    x3p_non_ctrl =  models.IntegerField()
    nofr =  models.IntegerField()
    total_glance_view =  models.IntegerField()
    class Meta:
        unique_together = ('product_group','MarketPlace_Id','week_ending')


class Ft_category(models.Model):
    product_group = models.CharField(max_length=20)
    MarketPlace_Id = models.IntegerField()
    category = models.CharField(max_length=40)
    week_ending = models.DateField()
    total_ft_p = models.FloatField()
    ft_retail_p = models.FloatField()
    ft_fba_p = models.FloatField()
    ctrl_p = models.FloatField()
    x3p_ctrl_p = models.FloatField()
    x3p_non_ctrl_p = models.FloatField()
    nofr_p = models.FloatField()      
    total_ft = models.IntegerField()
    ft_retail =  models.IntegerField()
    ft_fba =  models.IntegerField()
    ctrl =  models.IntegerField()
    x3p_ctrl =  models.IntegerField()
    x3p_non_ctrl =  models.IntegerField()
    nofr =  models.IntegerField()
    total_glance_view =  models.IntegerField()
    class Meta:
        unique_together = ('product_group','MarketPlace_Id','category','week_ending')


class Ft_brand(models.Model):
    product_group = models.CharField(max_length=20)
    MarketPlace_Id = models.IntegerField()
    brand = models.CharField(max_length=100)
    week_ending = models.DateField()
    total_ft_p = models.FloatField()
    ft_retail_p = models.FloatField()
    ft_fba_p = models.FloatField()
    ctrl_p = models.FloatField()
    x3p_ctrl_p = models.FloatField()
    x3p_non_ctrl_p = models.FloatField()
    nofr_p = models.FloatField()      
    total_ft = models.IntegerField()
    ft_retail =  models.IntegerField()
    ft_fba =  models.IntegerField()
    ctrl =  models.IntegerField()
    x3p_ctrl =  models.IntegerField()
    x3p_non_ctrl =  models.IntegerField()
    nofr =  models.IntegerField()
    total_glance_view =  models.IntegerField()
    class Meta:
        unique_together = ('product_group','MarketPlace_Id','brand','week_ending')

