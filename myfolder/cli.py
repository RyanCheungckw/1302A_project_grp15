import argparse
from ascii_pic.converter import convert_to_ascii_colored

def main():
    parser = argparse.ArgumentParser(description="進階終端機圖片轉 ASCII 藝術工具")
    parser.add_argument("image", help="圖片檔案路徑")
    parser.add_argument("-w", "--width", type=int, default=80, help="輸出寬度 (預設: 80)")
    parser.add_argument("-c", "--no-color", action="store_true", help="停用彩色輸出（僅顯示純文字）")
    parser.add_argument("-o", "--output", type=str, help="將結果儲存至指定的文字檔案")
    
    args = parser.parse_args()
    
    # 執行轉換
    result = convert_to_ascii_colored(args.image, new_width=args.width, color=not args.no_color)
    
    # 輸出結果到終端機
    print(result)
    
    # 若有指定輸出檔案則進行寫入
    if args.output:
        # 寫入檔案時建議移除 ANSI 色彩碼保持純淨
        plain_result = convert_to_ascii_colored(args.image, new_width=args.width, color=False)
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(plain_result)
        print(f"\n[成功] ASCII 藝術已儲存至: {args.output}")

if __name__ == "__main__":
    main()
