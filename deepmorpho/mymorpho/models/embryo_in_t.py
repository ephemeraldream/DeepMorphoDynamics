from django.db import models
from django.db.models import IntegerChoices
from django.utils.translation import gettext_lazy as _

from mymorpho.models.embryo import Embryo
from mymorpho.models.whole_image import WholeImage

class ClassType(IntegerChoices):
    ZERO = 0
    FIRST = 1
    SECOND = 2
    THIRD = 3



class EmbryoInT(models.Model):
    image = models.ImageField(verbose_name="Нарезанная картинка")
    source_image = models.ForeignKey(WholeImage,verbose_name="Картинка из которой нарезан кадр", on_delete=models.DO_NOTHING)
    embryo = models.ForeignKey(Embryo, verbose_name="Название Эмбриона", on_delete=models.DO_NOTHING)
    class_type = models.IntegerField(choices=ClassType.choices, verbose_name="Метка класса")
    well_number = models.IntegerField(verbose_name="Номер лунки.")



