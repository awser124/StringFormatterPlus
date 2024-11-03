import unittest
from StringFormatterPlus.SFP import *

class TestFStringProp(unittest.TestCase):

    # 测试正常路径：正常输入情况下的格式化
    def test_format_normal(self):
        fsp = FStringProp("Alice", Alignment.LEFT, 10)
        self.assertEqual(fsp.format(), "Alice<<<<<<")  # 左对齐

    # 测试正常路径：右对齐的格式化
    def test_format_right(self):
        fsp = FStringProp("Bob", Alignment.RIGHT, 10)
        self.assertEqual(fsp.format(), ">>>>>>Bob")  # 右对齐

    # 测试正常路径：居中对齐的格式化
    def test_format_center(self):
        fsp = FStringProp("Charlie", Alignment.CENTER, 11)
        self.assertEqual(fsp.format(), "===Charlie===")  # 居中对齐

    # 测试正常路径：正常对齐的格式化
    def test_format_normal_alignment(self):
        fsp = FStringProp("Dana", Alignment.NORMAL)
        self.assertEqual(fsp.format(), "Dana")  # 正常对齐，不添加任何填充符

    # 边界情况：字符串长度等于宽度
    def test_format_length_equal_to_width(self):
        fsp = FStringProp("Eve", Alignment.LEFT, 3)
        self.assertEqual(fsp.format(), "Eve")  # 应该不添加填充符

    # 边界情况：字符串长度大于宽度
    def test_format_length_greater_than_width(self):
        fsp = FStringProp("Franklin", Alignment.LEFT, 5)
        self.assertEqual(fsp.format(), "Franklin")  # 应该不添加填充符

    # 边界情况：宽度为0
    def test_format_width_zero(self):
        fsp = FStringProp("Grace", Alignment.CENTER, 0)
        self.assertEqual(fsp.format(), "Grace")  # 应该返回原字符串

    # 边界情况：空字符串
    def test_format_empty_string(self):
        fsp = FStringProp("", Alignment.LEFT, 10)
        self.assertEqual(fsp.format(), "<<<<<<<<<")  # 空字符串的左对齐

# 运行单元测试
if __name__ == '__main__':
    unittest.main()
