from dataclasses import dataclass
from pathlib import Path

import torch
from dl_folder.models import cnn_model
from mymorpho.models.whole_image import WholeImage
from PIL import Image as PILmage
from torchvision.transforms.functional import pil_to_tensor


@dataclass
class Coordinates:
    classification_pred: list
    regression_pred: list
    hole_pred: list
    pil_image: PILmage
    tensor: torch.Tensor


model = cnn_model.EmbryoModel()
model.load_state_dict(
    torch.load(Path(__file__).resolve().parent.parent / "first_step_model")
)
model.eval()


def gen_labels(inst: WholeImage) -> PILmage:
    image = PILmage.open(inst.image)
    tensor = pil_to_tensor(image)
    tensor_source = tensor.clone().detach()
    tensor = tensor / 255
    tensor = tensor.unsqueeze(0)

    with torch.no_grad():
        reg_pred, cls_pred, hole_pred = model(tensor)

    cls_pred = cls_pred.squeeze(0)
    reg_pred = reg_pred.squeeze(0)

    _, cls_pred = torch.max(cls_pred, dim=1)
    cls_pred = cls_pred.tolist()
    reg_pred = reg_pred * 255
    reg_pred = reg_pred.tolist()
    hole_pred = 1 if torch.ge(hole_pred, 0.5).item() is False else 0

    return Coordinates(cls_pred, reg_pred, hole_pred, image, tensor_source)
