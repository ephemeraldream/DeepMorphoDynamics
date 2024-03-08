from django.db import models


class MarkerTree(models.Model):
    mt_id = models.IntegerField(primary_key=True)
    mt_parent = models.IntegerField(default=0, verbose_name="Родительский маркер")
    mt_primary = models.BooleanField(default=True)
    mt_stored_data = models.TextField(null=True, blank=True)
    mt_marker_type = models.IntegerField(null=True, blank=True)
    mt_ins_from = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
    )
    mt_ins_to = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
    )
    mt_stored_data_short = models.TextField(null=True, blank=True)
    mt_label = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name="Метка для отображения",
    )

    class Meta:
        db_table = "marker_tree"
        verbose_name = "Линеаризированное дерево маркеров"
        verbose_name_plural = "Линеаризированные деревья маркеров"
