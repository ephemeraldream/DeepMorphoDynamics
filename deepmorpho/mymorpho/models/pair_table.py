from django.db import models


import uuid


class PairTable(models.Model):
    pr_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pr_idf = models.UUIDField(
        default=uuid.uuid4, editable=False
    )  # TODO: why editable=False?
    pr_idm = models.UUIDField(default=uuid.uuid4, editable=False)
    pt_infertilitytype = models.BooleanField(null=True)
    pt_bdatem = models.DateField()
    pt_bdatef = models.DateField()

    class Meta:
        db_table = "pair_table"
        verbose_name = "Обезличеннная информация о родителях"
        verbose_name_plural = "Обезличеннная информация о родителях"
