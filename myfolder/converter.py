from PIL import Image

# 由暗到亮的字元集
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    """調整圖片大小以適應終端機寬度，同時保持長寬比"""
    width, height = image.size
    aspect_ratio = height / width
    # 終端機字元通常高度大約是寬度的 2 倍，因此乘上 0.55 進行修正
    new_height = int(new_width * aspect_ratio * 0.55)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    """將圖片轉換為灰階"""
    return image.convert("L")

def pixels_to_ascii(image):
    """將每個像素轉換為對應的 ASCII 字元"""
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters

def convert_image_to_ascii(image_path, new_width=100):
    """主轉換函式"""
    try:
        image = Image.open(image_path)
    except Exception as e:
        return f"無法開啟圖片: {e}"
    
    resized_image = resize_image(image, new_width)
    grayscale_image = grayify(resized_image)
    
    ascii_str = pixels_to_ascii(grayscale_image)
    img_width = grayscale_image.width
    
    # 按照圖片寬度將字串分割成多行
    ascii_img = "\n".join([ascii_str[i:(i + img_width)] for i in range(0, len(ascii_str), img_width)])
    return ascii_img
