from PIL import Image, ImageEnhance, ImageOps, ImageFilter
import random
import os

class DataAugment:
    def __init__(self, image_folder):
        self.image_folder = image_folder

    def _random_rotate(self, image):
        angle = random.randint(-30, 30)
        return image.rotate(angle)

    def _random_flip(self, image):
        return ImageOps.mirror(image)

    def _random_brightness(self, image):
        enhancer = ImageEnhance.Brightness(image)
        return enhancer.enhance(random.uniform(0.5, 1.5))

    def _random_contrast(self, image):
        enhancer = ImageEnhance.Contrast(image)
        return enhancer.enhance(random.uniform(0.5, 1.5))

    def random_shear(self, image):
        shear_factor = random.uniform(-0.2, 0.2)
        return image.transform(image.size, Image.AFFINE, (1, shear_factor, 0, 0, 1, 0))

    def random_translate(self, image):
        translate_factor = random.randint(-50, 50)
        return image.transform(image.size, Image.AFFINE, (1, 0, translate_factor, 0, 1, translate_factor))

    def random_zoom(self, image):
        zoom_factor = random.uniform(1, 1.5)
        return image.transform(image.size, Image.AFFINE, (zoom_factor, 0, 0, 0, zoom_factor, 0))

    def random_crop(self, image):
        crop_factor = random.uniform(0.5, 1)
        width, height = image.size
        new_width, new_height = int(width * crop_factor), int(height * crop_factor)
        left = random.randint(0, width - new_width)
        top = random.randint(0, height - new_height)
        right = left + new_width
        bottom = top + new_height
        return image.crop((left, top, right, bottom))

    def blur(self, image):
        return image.filter(ImageFilter.BLUR)

    def sharpen(self, image):
        return image.filter(ImageFilter.SHARPEN)

    def edge_enhance(self, image):
        return image.filter(ImageFilter.EDGE_ENHANCE)

    def smooth(self, image):
        return image.filter(ImageFilter.SMOOTH)

    def augment(self, image_path):
        image = Image.open(image_path)
        augmentations = [
            # self._random_rotate,
            # self._random_flip,
            self._random_brightness,
            self._random_contrast,
            self.random_shear,
            self.random_translate,
            self.random_zoom,
            self.random_crop,
            self.blur,
            self.sharpen,
            # self.edge_enhance,
            # self.smooth
        ]

        random_augmentations = []
        for i in range(IMAGE_AUGMENTATION_COUNT):
            random_augmentations.append(random.sample(augmentations, random.randint(2, 4)))
        augmented_images = [image]
        for augmentation in random_augmentations:
            augmented_image = image
            for augmentation_function in augmentation:
                augmented_image = augmentation_function(augmented_image)
            augmented_images.append(augmented_image)

        return augmented_images

    def augment_images_in_folder(self):
        for filename in os.listdir(self.image_folder):
            # Now each folder without a . in the name will be considered as a folder with sub_images
            if os.path.isdir(os.path.join(self.image_folder, filename)):
                sub_folder = os.path.join(self.image_folder, filename)
                for sub_filename in os.listdir(sub_folder):
                    if sub_filename.endswith(".jpg") or sub_filename.endswith(".png"):
                        image_path = os.path.join(sub_folder, sub_filename)
                        augmented_images = self.augment(image_path)
                        for i, image in enumerate(augmented_images):
                            class_name = sub_folder.split('/')[-1]
                            full_output_folder = os.path.join(OutputFolder, class_name)
                            sub_filename_path = os.path.join(full_output_folder, sub_filename)
                            print(sub_filename_path)
                            image.save(f"{sub_filename.split('.')[0]}_{i}.jpg")

IMAGE_AUGMENTATION_COUNT = 5

OutputFolder = '/Users/kkallurupalli/codebase/berk/GSVData/AugmentedImages/'
data_folder = '/Users/kkallurupalli/codebase/berk/GSVData/Images/'
data_augment = DataAugment(data_folder)
data_augment.augment_images_in_folder()