from django.db import models


class WellTimelineFrames(models.Model):
    wtf_wtl_id = models.IntegerField(primary_key=True, verbose_name="Идентификатор (номер) серии")
    wtf_ed_uuid = models.UUIDField(verbose_name="Идентификатор эмбриона")
    wtf_rel_focus = models.IntegerField(
        verbose_name="Относительная фокальная плоскость"
    )
    wtf_frame = models.BinaryField(verbose_name="Кадр (bmp)")
    wtf_dif = models.IntegerField(default=0, verbose_name="Разница с предыдущим кадром")
    wtf_stabilized = models.BooleanField(
        default=False, verbose_name="Признак выполнения стабилизации"
    )

    class Meta:
        db_table = "well_timeline_frames"
        unique_together = [["wtf_wtl_id", "wtf_ed_uuid", "wtf_rel_focus"]]
        verbose_name = "Кадры серии изображений"
        verbose_name_plural = "Кадры серий изображений"


