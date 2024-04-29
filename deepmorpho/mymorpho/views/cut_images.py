import cv2
import numpy as np
import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt



def cut_images(request, patch_size_ratio=0.08):

    data = json.loads(request.body)
    # Вычисляем размер кубика как 8% от меньшей стороны изображения
    patch_size = int(min(data.image.shape[0], data.image.shape[1]) * patch_size_ratio)
    half_size = patch_size // 2  # Размер половины кубика для вычисления границ

    patches = []

    # Проходимся по всем координатам
    for x, y in data.coordinates:
        # Проверяем, что координаты находятся в пределах изображения и не являются маленькими (мусорными) значениями
        if x > 5 and y > 5 and (x + half_size) < data.image.shape[1] and (y + half_size) < image.shape[0] and (
                x - half_size) > 0 and (y - half_size) > 0:
            # Вырезаем кубик с центром в (x, y)
            patch = data.image[y - half_size:y + half_size, x - half_size:x + half_size]
            patches.append(patch)

    return patches
