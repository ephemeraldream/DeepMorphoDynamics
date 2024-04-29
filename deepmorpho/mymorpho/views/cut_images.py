from mymorpho.views.first_network import Coordinates


def cut_images(coordinates: Coordinates, patch_size_ratio=0.08):
    # Вычисляем размер кубика как 8% от меньшей стороны изображения
    patch_size = int(
        min(coordinates.tensor.shape[0], coordinates.tensor.shape[1]) * patch_size_ratio
    )
    # TODO: FIX THIS!!!
    # half_size = patch_size // 2  # Размер половины кубика для вычисления границ
    half_size = 7

    patches = []

    # Проходимся по всем координатам
    for x, y in coordinates.regression_pred:
        # Проверяем, что координаты находятся в пределах изображения и не являются маленькими (мусорными) значениями
        if (
            x > 5 and y > 5
            # TODO: FIX THIS!!!
            # and (x + half_size) < coordinates.image.shape[1]
            # and (y + half_size) < coordinates.image.shape[0]
            # and (x - half_size) > 0
            # and (y - half_size) > 0
        ):
            # Вырезаем кубик с центром в (x, y)
            test = [y - half_size, y + half_size, x - half_size, x + half_size]
            patch = coordinates.tensor[
                0,
                int(y - half_size) : int(y + half_size),
                int(x - half_size) : int(x + half_size),
            ]
            patches.append(patch)

    return patches
