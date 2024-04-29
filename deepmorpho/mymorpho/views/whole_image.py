from mymorpho.models.embryo_in_t import EmbryoInT
from django.core.files.base import ContentFile
import io
from torchvision.transforms.functional import to_pil_image
from mymorpho.models.embryo import Embryo
from mymorpho.views.cut_images import cut_images
from mymorpho.views.first_network import gen_labels
from mymorpho.models.whole_image import WholeImage
from rest_framework import viewsets
from mymorpho.serializers import (
    EmbryoInTSerializer,
    WholeImageSerializer,
    WholeImagesSerializer,
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from drf_spectacular.utils import extend_schema_view, extend_schema


@extend_schema_view(
    # list=extend_schema(summary="Получить список изображений"),
    create=extend_schema(
        summary="Загрузить изображения",
        request={"multipart/form-data": WholeImageSerializer(many=True)},
    ),
    retrieve=extend_schema(summary="Получить изображение"),
    update=extend_schema(summary="Обновить изображение"),
    destroy=extend_schema(summary="Удалить изображение"),
)
class WholeImageViewSet(viewsets.ModelViewSet):
    queryset = WholeImage.objects.all()
    serializer_class = WholeImagesSerializer
    permission_classes = [AllowAny]

    # TODO: сделать валидацию хешированием на то, что такой файл уже не присутстует в БД?
    def create(self, request, *args, **kwargs):
        serializer = WholeImagesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        whole_images: list[WholeImage] = []

        for image in serializer.validated_data["images"]:
            # TODO: добавить обработку всех файлов, а не только одного
            time = image.name
            if "." not in time:
                raise ValidationError("Название файла не содержит расширение.")
            time = time.split(".")[0]
            if not time.isdigit():
                raise ValidationError("Имя файла должно содержать только цифры.")

            instance = WholeImage(**{"image": image, "time": time})
            instance.save()
            whole_images.append(instance)

        pictures_of_cells = cut_images(gen_labels(whole_images[0]))
        embryos: list[Embryo] = []
        for i in range(len(pictures_of_cells)):
            embryo = Embryo(name=None)  # TODO: костыль убрать
            embryo.save()
            embryos.append(embryo)

        embryo_captures: list[int] = []
        for source_image_instance in whole_images:
            pictures_of_cells = cut_images(gen_labels(source_image_instance))
            for i, picture_of_cell in enumerate(pictures_of_cells):
                image_pil = to_pil_image(
                    picture_of_cell
                )  # предполагается, что это объект PIL Image
                buffer = io.BytesIO()
                image_pil.save(buffer, format="JPEG")
                image_file = ContentFile(buffer.getvalue())

                embryo_in_t = EmbryoInT(
                    image=image_file,
                    source_image=source_image_instance,
                    embryo=embryos[i],
                    class_type=None,
                    well_number=i,
                )
                embryo_in_t.save()
                embryo_captures.append(embryo_in_t.pk)

        return Response(
            EmbryoInTSerializer(
                EmbryoInT.objects.filter(pk__in=embryo_captures), many=True
            ).data
        )
