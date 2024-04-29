from django.db import models



class WholeImage(models.Model):
    image = models.ImageField(verbose_name="Ненарезанная целая картинка")
    time = models.IntegerField(verbose_name="Порядковый номер картинки")


