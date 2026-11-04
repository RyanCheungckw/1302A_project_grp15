import argparse
from ascii_pic.converter import convert_image_to_ascii

def main():
    parser = argparse.ArgumentParser(description="將圖片轉換為終端機 ASCII 藝術字元畫")
    parser.add_argument("image", help="圖片檔案路徑")
    parser.add_argument("-w", "--width", type=int, default=80, help="輸出寬度 (預設: 80)")
    
    args = parser.parse_args()
    
    result = convert_image_to_ascii(args.image, new_width=args.width)
    print(result)

if __name__ == "__main__":
    main()
