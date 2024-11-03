class Alignment:
    LEFT = 'left'
    CENTER = 'center'
    RIGHT = 'right'
    NORMAL = 'normal'
    NONE = 'none'


class FStringProp:
    def __init__(self, name, alignment=Alignment.LEFT, width=10):
        self.name = name if isinstance(name, str) else str(name)  # 确保 name 是字符串
        self.alignment = alignment
        self.width = width

    def format(self):
        return self.format_value(self.name, self.alignment, self.width)

    @staticmethod
    def format_value(text, alignment=Alignment.NORMAL, width=10):
        if width < 0:
            width = 0  # 确保宽度不能为负值

        formatted_text = text
        padding = max(0, width - len(text))  # 计算需要的填充数量

        # 根据对齐方式生成格式化文本
        if alignment == Alignment.CENTER:
            left_padding = padding // 2
            right_padding = padding - left_padding
            formatted_text = ' ' * left_padding + text + ' ' * right_padding
        elif alignment == Alignment.RIGHT:
            formatted_text = ' ' * padding + text
        elif alignment == Alignment.LEFT:
            formatted_text = text + ' ' * padding
        elif alignment == Alignment.NORMAL:
            left_padding = padding // 2
            right_padding = padding - left_padding
            formatted_text = ' ' * left_padding + text + ' ' * right_padding
        elif alignment == Alignment.NONE:
            formatted_text = text

        return formatted_text.strip()  # 返回去除前后空格的字符串


class Formatter:
    @staticmethod
    def format(strings, *values):
        result = ''

        for i in range(len(strings)):
            result += strings[i]  # 添加字符串部分
            if i < len(values):
                # 检查值并格式化
                if isinstance(values[i], FStringProp):
                    result += values[i].format()  # 调用格式化方法
                elif isinstance(values[i], str) and '|' in values[i]:
                    text, alignment, width_str = values[i].split('|')
                    width = int(width_str) if width_str.isdigit() else 10  # 默认宽度为10
                    if width < 0:
                        width = 0  # 确保宽度不能为负值
                    result += FStringProp.format_value(text, alignment, width)  # 静态调用格式化方法
                else:
                    result += str(values[i])  # 直接添加其他类型的值

        return result  # 返回格式化后的字符串


class Sample:
    @staticmethod
    def run():
        name = 'Alice'
        age = 25
        salary = 5000
        formatted_name = FStringProp(name, Alignment.CENTER, 11).format()  # 确保调用 format 方法
        formatted_age = FStringProp.format_value(str(age), Alignment.LEFT, 3)  # 添加对齐和宽度
        formatted_salary = FStringProp.format_value(str(salary), Alignment.RIGHT, 7)  # 添加对齐和宽度

        formatted_string = Formatter.format(
            f"Hello, {name}!\n"
            f"Your age is {formatted_age} and your salary is {formatted_salary}.\n"
            f"You are {formatted_name}."
        )
        print(formatted_string)


if __name__ == '__main__':
    # 运行示例
    Sample.run()
