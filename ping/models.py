from django.db import models

# Create your models here.
class Hosts(models.Model):
    ping_id = models.BigAutoField(primary_key=True)
    host_name = models.CharField(blank=False, max_length=1000, verbose_name='Server hostname')
    alias = models.CharField(blank=True, max_length=1000, verbose_name='Display name')
    category = models.CharField(blank=True, max_length=1000, verbose_name='Category')
    
    class Meta:
        managed = False
        db_table = 'ping'
        verbose_name = 'Host entry'
        verbose_name_plural = 'Hosts entries'
        ordering = ['host_name']
    
    def __str__(self):
        return '%s (%s) - %s' % (self.host_name, self.alias, self.category)

class Sites(models.Model):
    website_id = models.BigAutoField(primary_key=True)
    url = models.CharField(blank=False, max_length=1000, verbose_name='Server url (incl http)')
    alias = models.CharField(blank=True, max_length=1000, verbose_name='Display name')
    category = models.CharField(blank=True, max_length=1000, verbose_name='Category')
    
    class Meta:
        managed = False
        db_table = 'websites'
        verbose_name = 'URL entry'
        verbose_name_plural = 'URL entries'
        ordering = ['url']
    
    def __str__(self):
        return '%s (%s) - %s' % (self.alias, self.url, self.category)