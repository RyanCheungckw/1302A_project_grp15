from PIL import Image

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=80):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)
    return image.resize((new_width, new_height))

def convert_to_ascii_colored(image_path, new_width=80, color=True):
    """將圖片轉換為帶有色彩或純文字的 ASCII 藝術"""
    try:
        image = Image.open(image_path)
    except Exception as e:
        return f"無法開啟圖片: {e}"
    
    image = resize_image(image, new_width)
    img_width, img_height = image.size
    
    ascii_output = []
    
    for y in range(img_height):
        row_str = ""
        for x in range(img_width):
            pixel = image.getpixel((x, y))
            
            # 支援 RGB 或 RGBA 圖片
            if isinstance(pixel, tuple):
                if len(pixel) == 4 and pixel[3] == 0:  # 處理透明背景
                    r, g, b = 255, 255, 255
                else:
                    r, g, b = pixel[0], pixel[1], pixel[2]
                # 計算灰階亮度 (0 - 255)
                gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            else:
                gray = pixel
                r, g, b = gray, gray, gray

            # 對應 ASCII 字元
            char_index = gray * (len(ASCII_CHARS) - 1) // 255
            char = ASCII_CHARS[char_index]
            
            if color:
                # 使用 ANSI 24位元色彩讓終端機顯示原圖色彩
                row_str += f"\033[38;2;{r};{g};{b}m{char}\033[0m"
            else:
                row_str += char
                
        ascii_output.append(row_str)
        
    return "\n".join(ascii_output)
