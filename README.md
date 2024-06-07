# city-photo-deep-learning
Predicting location based on photos

# Data
- Train/Validation data downloaded from https://www.kaggle.com/datasets/amaralibey/gsv-cities
- Test data can be downloaded from https://drive.google.com/drive/folders/1Eahccn3CL1sDkj3bdGUd5QIuDZGHsXT-?usp=drive_link or created from Test-Data-Creation-GoogleSV.ipynb, but you will need to get a Google API key.

# Model
- Trained model can be downloaded from https://drive.google.com/file/d/17zhQKmXCyXyZRABUbG-j5DvE9JNdiUGP/view?usp=drive_link

# preprocessing
- This folder contains different augment classes that were used to preprocess the data before fitting the model.

# EDA.ipynb
- Contains our eploratory data analysis code. We load in the dataframes from Kaggle, visualizing the distribution of images and photo year as well as looking at picture frequency by month and city.

# Create-Train-Val-Data.ipynb
- Loads in the same dataframes, however we randomly perform a 75-25 train/val split of the data which is saved in its own folders. We have them also saved into two csv files in this repo (test_df, train_df). To replicate our results, please use test_df and train_df to produce the same train/test split. We attempt to create custom batches where images from the same place id are in the same batch.

# Test-Data-Creation-GoogleSV.ipynb
- Uses the Google Street View APi to grab images from the same 23 major cities. We feed latitutude and longitutde coordinates from all cities to output images to those in the training and validation sets.

# trial-cnn.ipynb & CityCNN.ipynb
- We load in the train and validation data using Tensorflow's image_dataset_from_directory() function. We create our basic CNN model that has 6 convolutional layers with global max pooling and 1 dense layer. The second model created uses ResNet 50 as a backbone with 1 convolutional layer using global max pooling and 1 dense layer. The last model is the same as the second but we only train on some layers of ResNet. These are the 3 main models that we created.

# FinalModel.ipynb
- Uses the last model discussed above once with the augmented data and unagumented data and returns the train, validation and test accuracies.

# Gradio-App.ipynb
- Using the Gradio library, we load in our ResNet model and create two functions to first preprocess all the data and second to predict the location of the image. We launch the model through the interface function in built in Gradio to have a user add a image and our model returns one of the 23 city names.
