from django.db import models

from deepmorpho.mymorpho.models.embryo_data import EmbryoData


class WellTimeline(models.Model):
    wtl_id = models.AutoField(
        primary_key=True, verbose_name="Идентификатор (номер) серии"
    )
    wtl_ed_uuid = models.ForeignKey(
        EmbryoData,
        on_delete=models.CASCADE,
        related_name="well_timelines",
        verbose_name="Идентификатор эмбриона",
    )
    wtl_focus = models.SmallIntegerField(
        default=0,
        verbose_name="Главная фокальная плоскость в серии",
    )
    wtl_tempr = models.FloatField(verbose_name="Температура камеры культивирования")
    wtl_gas_co2 = models.CharField(
        max_length=255,
        verbose_name="Данные по CO2 в камере культивирования",
    )
    wtl_co2_concentration = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Концентрация CO2 в камере культивирования",
    )
    wtl_co2_flow = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Газовый поток CO2 в камере культивирования",
    )
    wtl_frame_dt = models.DateTimeField(verbose_name="Дата и время получения кадра")

    class Meta:
        db_table = "well_timeline"
        verbose_name = "Данные по серии изображений"
        verbose_name_plural = "Данные по сериям изображений"
