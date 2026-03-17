from PIL import Image
import os

img_dir = r"/Users/xiechangen/Downloads/20251211/20251211_07"
output_path = "/Users/xiechangen/Downloads/20251211/輸出wafer/7.jpg"

imgs_per_row = 8
total_imgs = 88

img_files = sorted([
    f for f in os.listdir(img_dir)
    if f.lower().endswith(('.jpg', '.jpeg', '.png'))
])

print(f"找到圖片數量：{len(img_files)}")

if len(img_files) < total_imgs:
    raise ValueError("圖片數量不足 88 張")

images = [Image.open(os.path.join(img_dir, f)) for f in img_files[:total_imgs]]

w, h = images[0].size
rows = total_imgs // imgs_per_row

merged_img = Image.new("RGB", (w * imgs_per_row, h * rows))

idx = 0
for row in range(rows):
    row_imgs = images[idx:idx + imgs_per_row]
    if row % 2 == 1:
        row_imgs = row_imgs[::-1]

    for col, img in enumerate(row_imgs):
        merged_img.paste(img, (col * w, row * h))

    idx += imgs_per_row

merged_img.save(output_path)
print("蛇字型組圖完成！")

