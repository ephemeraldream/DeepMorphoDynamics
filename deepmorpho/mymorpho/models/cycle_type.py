from django.db import models


class CycleType(models.Model):
    ct_id = models.SmallIntegerField(primary_key=True)
    ct_tname = models.CharField(max_length=8, verbose_name="Тип цикла")

    class Meta:
        db_table = "cycle_type"
        verbose_name = "Типы цикла, применяемые в системе"
        verbose_name_plural = "Типы цикла, применяемые в системе"
