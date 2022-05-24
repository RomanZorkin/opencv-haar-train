import logging
from pathlib import Path
from PIL import Image


logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

base_images_path = Path('')
convert_images_path = Path(base_images_path, 'tmp')
enclosures = (
    'negative_images',
    'positive_images',
)

target_size = (40, 40)
image_formats = {
    'png': {'ext': '.png', 'format': 'PNG'},
    'jpg': {'ext': '.jpg', 'format': 'JPEG'},
    'bmp': {'ext': '.bmp', 'format': 'BMP'},
}



def resize(target_size: tuple[int, int]) -> None:
    for enclosure in enclosures:
        target_path = Path(base_images_path, enclosure)
        convert_target_path = Path(convert_images_path, enclosure)
        images = [image for image in target_path.iterdir() if image.is_file()]
        err = 0
        for image_path in images:
            try:
                name = image_path.stem
                ext = image_path.suffix

                image = Image.open(image_path)
                image_size_old = image.size
                image = image.resize(target_size)
                image_size_new = image.size
                logger.info(f'For file {name}{ext} size {image_size_old} convert to {image_size_new}')
                new_path = Path(convert_target_path, f'{name}{ext}')
                if image.mode in ("RGBA", "P"):
                    image = image.convert("RGB")
                image.save(new_path)
                logger.info(f'File save to {new_path}')
            except:
                err += 1

        logger.info(err)

def reformat(new_format: str) -> None:
    for enclosure in enclosures:
        target_path = Path(base_images_path, enclosure)
        convert_target_path = Path(convert_images_path, enclosure)
        images = [image for image in target_path.iterdir() if image.is_file()]
        err = 0
        for image_path in images:
            try:
                name = image_path.stem
                new_name = f'{name}{image_formats[new_format]["ext"]}'
                format_tag = image_formats[new_format]['format']
                image = Image.open(image_path)
                new_path = Path(convert_target_path, new_name)
                if image.mode in ("RGBA", "P"):
                    image = image.convert("RGB")
                image.save(new_path, format_tag)
                logger.info(f'File save as: {new_path}')
            except:
                err += 1

        logger.info(err)


def rename(base_name: str = 'image') -> None:
    for enclosure in enclosures:
        target_path = Path(base_images_path, enclosure)
        convert_target_path = Path(convert_images_path, enclosure)
        images = [image for image in target_path.iterdir() if image.is_file()]
        err = 0
        for num, image_path in enumerate(images):
            try:
                ext = image_path.suffix
                image = Image.open(image_path)
                new_name =f'{enclosure}{base_name}{num}{ext}'
                new_path = Path(convert_target_path, new_name)
                if image.mode in ("RGBA", "P"):
                    image = image.convert("RGB")
                image.save(new_path)
                logger.info(f'File save as: {new_path}')
            except:
                err += 1

        logger.info(err)

resize(target_size)
#reformat('png')
#rename()
