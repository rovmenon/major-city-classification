import tensorflow as tf

class DataAugment:
    def __init__(self, train_data):
        self.train_data = train_data

    def adjust_brightness(self, image, delta):
        return tf.image.adjust_brightness(image, delta=delta)

    def adjust_contrast(self, image, contrast_factor):
        return tf.image.adjust_contrast(image, contrast_factor=contrast_factor)

    #def random_flip(self, image):
       # return tf.image.random_flip_left_right(image)

    #def random_rotate(self, image):
       # angle = tf.random.uniform(shape=[], minval=-30, maxval=30, dtype=tf.int32)
        #return tf.image.rot90(image, k=angle // 90)

    #def random_shift(self, image):
        #shift_width = tf.random.uniform(shape=[], minval=-20, maxval=20, dtype=tf.int32)
        #shift_height = tf.random.uniform(shape=[], minval=-20, maxval=20, dtype=tf.int32)
        #return tf.roll(image, shift=[shift_width, shift_height], axis=[0, 1])
    
    def augment_data(self, delta, contrast_factor):
        augmented_data = self.train_data.map(lambda x, y: (self.adjust_brightness(x, delta), y))
        augmented_data = augmented_data.map(lambda x, y: (self.adjust_contrast(x, contrast_factor), y))
        #augmented_data = augmented_data.map(lambda x, y: (self.random_flip(x), y))
        #augmented_data = augmented_data.map(lambda x, y: (self.random_rotate(x), y))
        #augmented_data = augmented_data.map(lambda x, y: (self.random_shift(x), y))
        
        return augmented_data
