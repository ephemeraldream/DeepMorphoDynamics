from django.db import models


class EmbryoFocus(models.Model):
    ef_ed_uuid = models.UUIDField(verbose_name="Идентификатор эмбриона")
    ef_focus = models.SmallIntegerField(verbose_name="Главная фокальная плоскость")
    ef_wtl_id = models.IntegerField(
        verbose_name="Идентификатор (номер) серии применения данной главной плоскости"
    )

    class Meta:
        db_table = "embryo_focus"
        unique_together = [["ef_ed_uuid", "ef_wtl_id"]]
        verbose_name = "Разметка главной фокальной плоскости эмбриона"
        verbose_name_plural = "Разметки главных фокальных плоскостей эмбрионов"
