import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy as np


path = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(path, 'lenna-mod.jpg')
filename2 = os.path.join(path, 'download.jpeg')


data = mpimg.imread(filename)
data2 = mpimg.imread(filename2)


data2_pil = Image.fromarray((data2 * 255).astype(np.uint8)) if data2.dtype == np.float32 else Image.fromarray(data2)
data2_resized = data2_pil.resize((100, 100))  


data2_resized_np = np.array(data2_resized)


fig, ax = plt.subplots()
ax.imshow(data)
ax.axis('off')


inset_width = 0.25  
inset_height = data2_resized_np.shape[0] / data.shape[0] * inset_width * data.shape[1] / data.shape[0]


inset_ax = fig.add_axes([0.7, 0.7, inset_width, inset_width * data2_resized_np.shape[0] / data2_resized_np.shape[1]])
inset_ax.imshow(data2_resized_np)
inset_ax.axis('off')

plt.show()
