import matplotlib.pyplot as plt
from image_utils import detect_edges
original_gray, edge_result = detect_edges('whatsapp_image.jpg', threshold=50)
plt.figure(figsize=(10, 5))
plt.imshow(edge_result, cmap='gray')
plt.title("White Edges")
plt.axis('off')
plt.show()
