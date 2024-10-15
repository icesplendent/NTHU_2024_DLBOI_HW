import torch
from torchvision import transforms
from PIL import Image

# Load the image
image_path = "path_to_your_image.jpg"
image = Image.open("C:/Users/USER/desktop/DL_biotech/Hw3/chest_xray/test/NORMAL/IM-0003-0001.jpeg")

# Define a transform to convert the image to a tensor
transform = transforms.ToTensor()
image_tensor = transform(image)

# Print the image tensor
print(image_tensor)