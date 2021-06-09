from django.db import models

class Timescan(models.Model):
    # id = models.AutoField()
    site_code = models.CharField(max_length=15)
    date_scan = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    sh_code = models.CharField(max_length=5, blank=True, null=True)
    sh_name = models.CharField(max_length=50, blank=True, null=True)
    d_code = models.CharField(max_length=50, blank=True, null=True)
    user_code = models.CharField(max_length=10, blank=True, null=True)
    site_name = models.CharField(max_length=100, blank=True, null=True)
    date_save = models.DateTimeField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)
    date_process = models.DateTimeField(blank=True, null=True)
    op1 = models.CharField(max_length=1, blank=True, null=True)
    op2 = models.CharField(max_length=1, blank=True, null=True)
    op3 = models.CharField(max_length=1, blank=True, null=True)
    op4 = models.CharField(max_length=1, blank=True, null=True)
    op5 = models.CharField(max_length=1, blank=True, null=True)
    upd_date = models.DateTimeField(db_column='UPD_date', blank=True, null=True)
    upd_by = models.CharField(db_column='UPD_by', max_length=25, blank=True, null=True)
    upd_flag = models.CharField(db_column='UPD_flag', max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Timescan'