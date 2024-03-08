from django.db import models


import uuid
from deepmorpho.mymorpho.models.cycle_type import CycleType

from deepmorpho.mymorpho.models.pair_table import PairTable


class EmbryoData(models.Model):
    ed_uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="Идентификатор эмбриона",
    )
    ed_pr_id = models.ForeignKey(
        PairTable,
        on_delete=models.CASCADE,
        verbose_name="Идентификатор пары",
    )
    ed_id = models.SmallIntegerField(verbose_name="Номер лунки")
    ed_cs_id = models.ForeignKey(
        CycleType,
        on_delete=models.CASCADE,
        verbose_name="Идентификатор цикла",
    )
    ed_destiny = models.CharField(
        max_length=4,
        verbose_name="Назначение эмбриона",
    )
    ed_mainfocus = models.SmallIntegerField(
        default=0, verbose_name="Базовый фокус при создании"
    )
    ed_focus_min = models.SmallIntegerField(
        null=True, blank=True, verbose_name="Нижняя граница фокуса в сериях"
    )
    ed_focus_max = models.SmallIntegerField(
        null=True, blank=True, verbose_name="Верхняя граница фокуса в сериях"
    )
    ed_own = models.BooleanField(
        default=True, verbose_name="Признак собственного ооцита"
    )
    ed_fresh = models.BooleanField(
        default=True, verbose_name="Признак 'свежий/размороженный'"
    )
    ed_biodate = models.DateField(null=True, blank=True, verbose_name="Дата биопсии")
    ed_fertilization = models.SmallIntegerField(
        null=True, blank=True, verbose_name="Количество пронуклеусов при оплодотворении"
    )
    ed_seriescount = models.IntegerField(
        default=0, verbose_name="Количество серий изображений"
    )
    ed_pn_size_rate = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Соотношение размеров пронуклеусов",
    )
    ed_insemination = models.DateTimeField(
        null=True, blank=True, verbose_name="Дата и время инсеминации (оплодотворения)"
    )
    ed_iceps = models.BooleanField(
        default=False, verbose_name="Признак наличия неоднородности цитоплазмы (ЭПС)"
    )
    ed_icinc = models.BooleanField(
        default=False,
        verbose_name="Признак наличия неоднородности цитоплазмы (прочие включения)",
    )
    ed_anom_form = models.BooleanField(
        default=False, verbose_name="Признак наличия аномальной формы"
    )
    ed_cl2_sz = models.BooleanField(
        default=False,
        verbose_name="Равномерность бластомеров после 2-клеточной стадии",
    )
    ed_cl3_sz = models.BooleanField(
        default=False,
        verbose_name="Равномерность бластомеров после 3-клеточной стадии",
    )
    ed_cl4_sz = models.BooleanField(
        default=False,
        verbose_name="Равномерность бластомеров после 4-клеточной стадии",
    )
    ed_cl5_sz = models.BooleanField(
        default=False,
        verbose_name="Равномерность бластомеров после 5-клеточной стадии",
    )
    ed_cl6_sz = models.BooleanField(
        default=False,
        verbose_name="Равномерность бластомеров после 6-клеточной стадии",
    )
    ed_cl8_sz = models.BooleanField(
        default=False,
        verbose_name="Равномерность бластомеров после 8-клеточной стадии",
    )
    ed_clrev = models.BooleanField(
        default=False,
        verbose_name="Реверсивное дробление",
    )
    ed_mnb = models.BooleanField(
        default=False,
        verbose_name="Мультинуклеация",
    )
    ed_vacuolization = models.BooleanField(
        default=False,
        verbose_name="Вакуолизация",
    )
    ed_frag = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Процент фрагментации",
    )
    ed_ins_method = models.SmallIntegerField(
        default=1,
        verbose_name="Метод инсеминации",
    )
    ed_finalscore = models.CharField(
        max_length=3,
        null=True,
        blank=True,
        verbose_name="Финальная оценка по Гарднеру",
    )
    ed_pn_start_time = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Время образования пронуклеусов",
    )
    ed_pn_ds_time = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Время исчезновения пронуклеусов",
    )
    ed_t2 = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Время деления до 2-клеточной стадии",
    )
    ed_t3 = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Время деления до 3-клеточной стадии",
    )
    ed_t4 = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Время деления до 4-клеточной стадии",
    )
    ed_t5 = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Время деления до 5-клеточной стадии",
    )
    ed_t6 = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Время деления до 6-клеточной стадии",
    )
    ed_t8 = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Время деления до 8-клеточной стадии",
    )
    ed_first_clvg_time = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Время первого деления",
    )
    ed_compact_start = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Начало компактизации",
    )
    ed_compacted_time = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Завершение компактизации",
    )
    ed_cavitation_start = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Начало кавитации",
    )
    ed_full_blast = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Время формирования полной бластоцисты",
    )
    ed_expand_time = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Время экспандирования бластоцисты",
    )
    ed_hatching_start = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Начало выхода из оболочки",
    )

    class Meta:
        db_table = "embryo_data"
        verbose_name = "Данные об эмбрионе"
        verbose_name_plural = "Данные об эмбрионах"
