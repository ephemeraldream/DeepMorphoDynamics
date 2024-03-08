from django.db import models


class WellTimelineMarker(models.Model):
    wtm_wtl_id = models.IntegerField(verbose_name="Идентификатор (номер) серии")
    wtm_focus = models.SmallIntegerField(
        verbose_name="Относительная фокальная плоскость"
    )
    wtm_ed_uuid = models.UUIDField(verbose_name="Идентификатор эмбриона")
    wtm_mark_id = models.IntegerField(verbose_name="Идентификатор маркера")
    wtm_mark_data = models.TextField(
        null=True, blank=True, verbose_name="Служебные данные маркера"
    )
    wtm_restrict_mark = models.IntegerField(verbose_name="Метка ограничения")

    class Meta:
        db_table = "well_timeline_marker"
        unique_together = [["wtm_wtl_id", "wtm_focus", "wtm_ed_uuid", "wtm_mark_id"]]
        verbose_name = "Маркер кадра"
        verbose_name_plural = "Маркеры кадров"