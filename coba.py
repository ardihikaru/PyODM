import os
from pyodm import Node
n = Node('localhost', 3000)

# import matplotlib.image as mpimg
# import matplotlib.pyplot as plt
#
# # Read Images
# img = mpimg.imread('examples/images/DSC01605.JPG')
#
# # Output Images
# plt.imshow(img)
# plt.show()

root_dir = "./"

img_data = [
    root_dir + 'examples/images/DSC01605.JPG',
    root_dir + 'examples/images/DSC01606.JPG',
    root_dir + 'examples/images/DSC01607.JPG',
    root_dir + 'examples/images/DSC01608.JPG',
    root_dir + 'examples/images/DSC01609.JPG',
    root_dir + 'examples/images/DSC01610.JPG',
    root_dir + 'examples/images/DSC01611.JPG',
    root_dir + 'examples/images/DSC01612.JPG',
    root_dir + 'examples/images/DSC01613.JPG',
    root_dir + 'examples/images/DSC01614.JPG'
]

task = n.create_task(img_data, {'dsm': True})
task.wait_for_completion()
print(os.listdir(task.download_assets("results"))[0:2])

print("done ..")