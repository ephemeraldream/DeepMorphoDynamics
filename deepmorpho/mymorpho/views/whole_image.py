from mymorpho.models.whole_image import WholeImage
from rest_framework import viewsets
from mymorpho.serializers import WholeImageSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

class WholeImageViewSet(viewsets.ModelViewSet):
    queryset = WholeImage.objects.all()
    serializer_class = WholeImageSerializer
    permission_classes = [AllowAny]
    # serializer.validated_data['image'].name
    @parser_classes([FormParser, MultiPartParser])
    def create(self, request, *args, **kwargs):
        serializer = WholeImageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        time = serializer.validated_data['image'].name
        if "." not in time:
            raise ValidationError("Название файла не содержит расширение.")
        time = time.split(".")[0]
        if not time.isdigit():
            raise ValidationError("Имя файла должно содержать только цифры.")


        instance = WholeImage(**{"image":request.data['image'],'time':time})
        instance.save()
        return Response(WholeImageSerializer(instance).data)



