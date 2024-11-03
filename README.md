# StringFormatterPlus
python StringFormatterPlus (SFP) Library 

---
### StringFormatterPlus 简介

**StringFormatterPlus** 是一个旨在提升字符串格式化体验的库，提供了灵活且强大的字符串格式化功能。通过简单易用的接口，用户可以轻松实现字符串的对齐、宽度控制和美观展示，使输出结果更具可读性。这个库特别适合于数据展示，例如表格输出、日志记录、界面/UI展示等场景，帮助开发者提高工作效率。

---
### 主要功能：

1. **多种对齐方式**：
   - 提供左对齐、居中对齐、右对齐、正常对齐和无对齐等多种对齐选项，满足不同场景下的字符串展示需求。如在数据表格中，用户可以选择将标题居中而将数据左对齐，提高整体整齐度。

2. **灵活的字符串格式化**：
   - 支持通过指定宽度和对齐方式对字符串进行格式化，确保输出的字符串在视觉上整齐划一。用户可以灵活设置每列的宽度，适应不同格式的需求，增强可读性。

3. **动态组合字符串**：
   - 允许用户将多个字符串和变量结合在一起，自动应用格式化规则，便于生成复杂的输出信息。如此一来，开发者可以快速地构建出格式化的报告或文档，省去手动拼接字符串的麻烦。

4. **简单易用的接口**：
   - 通过定义清晰的类和方法，用户可以快速上手，无需深入了解底层实现即可高效使用。伴随着详细的文档和示例代码，用户能够迅速掌握库的各种功能。
---
### 主要组成部分：

- **Alignment 类**：
  - 定义了格式化所需的各种对齐方式，用户可以选择最适合其需求的对齐选项。

- **FStringProp 类**：
  - 用于创建带有名称的字符串属性，支持对齐和宽度的格式化。该类帮助用户组织和管理需要格式化的字符串数据。

- **Formatter 类**：
  -提供静态方法，允许用户将多个字符串和格式化值结合输出，支持灵活的格式化策略。该类重用性高，能适应不同的字符串组合需求。

- **AdvancedFStringProp 类**：
  - 扩展了 FSStringProp 类，提供更高级的字符串格式化功能。用户可以使用自定义的格式字符串进行格式化，实现灵活且复杂的字符串展示。该类支持格式字符串中的字段替换，允许用户根据需要快速定义输出格式，适用于更复杂的格式化需求。
- **Sample 类**：
  - 示例用法，展示如何使用 StringFormatterPlus 库进行字符串格式化，包含基本用法和进阶技巧。
---
### 使用示例：

用户可以通过创建 `FStringProp` 对象，并定义所需的对齐方式和宽度，然后利用 `Formatter` 类将这些信息格式化为一段美观的输出，例如：

```python
formatted_name = FStringProp('Alice', Alignment.CENTER, 15).format()
formatted_age = FStringProp.format_value(str(30), Alignment.LEFT, 3)
formatted_salary = FStringProp.format_value(str(5000), Alignment.RIGHT, 10)

output = Formatter.format(
    f"Name: {formatted_name}\n"
    f"Age: {formatted_age}\n"
    f"Salary: {formatted_salary}"
)
```

#### 高级功能
```python
# 使用格式字符串
custom_format_string = "Name: {name}, Age: {age}, Salary: {salary}"
advanced_formatted_string = AdvancedFStringProp(name).format_with_format_string(custom_format_string)

print(formatted_string)
print(advanced_formatted_string)
```
StringFormatterPlus 使字符串处理变得更加高效和美观，是开发者处理和展示字符串数据的理想选择。无论是在简单的控制台输出，还是复杂的用户界面展示，它都能提供强有力的支持，提升用户的开发体验。
