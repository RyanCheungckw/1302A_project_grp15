import unittest
from PIL import Image
from ascii_pic.converter import resize_image, convert_to_ascii_colored

class TestAsciiConverter(unittest.TestCase):
    
    def setUp(self):
        """在每個測試執行前建立一個簡單的測試圖片"""
        self.test_image = Image.new("RGB", (50, 50), color="red")
        self.test_image_path = "/tmp/test_sample.png"
        self.test_image.save(self.test_image_path)

    def test_resize_image(self):
        """測試圖片縮放比例是否正確"""
        resized = resize_image(self.test_image, new_width=20)
        self.assertEqual(resized.width, 20)
        # 確保高度也有根據長寬比與字元高度修正
        self.assertTrue(resized.height > 0)

    def test_convert_to_ascii_plain(self):
        """測試純文字（無顏色）轉換是否能順利回傳字串"""
        result = convert_to_ascii_colored(self.test_image_path, new_width=20, color=False)
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        # 檢查是否含有換行符號（代表有多行 ASCII 藝術）
        self.assertIn("\n", result)

    def test_convert_to_ascii_colored(self):
        """測試彩色 ASCII 轉換是否包含 ANSI 色彩控制碼"""
        result = convert_to_ascii_colored(self.test_image_path, new_width=20, color=True)
        self.assertIsInstance(result, str)
        # 檢查是否包含 ANSI 24位元色彩的跳脫字元 \033[
        self.assertIn("\033[", result)

    def test_invalid_image_path(self):
        """測試當圖片路徑錯誤時是否能正確捕捉例外並回傳錯誤訊息"""
        result = convert_to_ascii_colored("non_existent_image.png", new_width=20)
        self.assertIn("無法開啟圖片", result)


if __name__ == "__main__":
    unittest.main()
