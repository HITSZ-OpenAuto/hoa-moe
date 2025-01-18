import re
import argparse
from pathlib import Path
import urllib.parse

def wrap_badges_with_div(content, div_classes="img-div hx-mt-4 hx-flex-row hx-justify-start hx-items-center"):
    """
    查找连续的 badge 行并用 div 包装
    
    Args:
        content (str): 要处理的文件内容
        div_classes (str): div 标签的类名
    """
    lines = content.split('\n')
    processed_lines = []
    
    # badge 行的正则表达式
    badge_pattern = r'!\[.*?\]\(https://img\.shields\.io/badge/.*?\)'

    i = 0
    while i < len(lines):
        # 如果当前行已经在 div 中，直接添加
        if '<div class="img-div' in lines[i]:
            while i < len(lines) and '</div>' not in lines[i]:
                line = lines[i]
                # Encode only the Chinese characters in the entire line
                line = re.sub(
                    badge_pattern,
                    lambda m: m.group(0).replace(m.group(0), re.sub(r'([\u4e00-\u9fff]+)', lambda c: urllib.parse.quote(c.group()), m.group(0))),
                    line
                )
                processed_lines.append(line)
                i += 1
            if i < len(lines):
                processed_lines.append(lines[i])  # 添加结束的</div>
            i += 1
            continue
            
        # 检查是否是 badge 行
        if re.search(badge_pattern, lines[i]):
            # 寻找连续的 badge 行
            badge_block = []
            while i < len(lines) and (re.search(badge_pattern, lines[i]) or lines[i].strip() == ''):
                line = lines[i]
                # Encode only the Chinese characters in the entire line
                line = re.sub(
                    badge_pattern,
                    lambda m: m.group(0).replace(m.group(0), re.sub(r'([\u4e00-\u9fff]+)', lambda c: urllib.parse.quote(c.group()), m.group(0))),
                    line
                )
                badge_block.append(line)
                i += 1
                
            if badge_block:
                # 添加 div 包装
                processed_lines.append(f'<div class="{div_classes}">\n')
                processed_lines.extend(badge_block)
                processed_lines.append('</div>\n')
        else:
            processed_lines.append(lines[i])
            i += 1
    
    return '\n'.join(processed_lines)

def process_file(file_path, div_classes, backup=False):
    """
    处理指定的 markdown 文件
    
    Args:
        file_path (Path): 文件路径
        div_classes (str): div 标签的类名
        backup (bool): 是否创建备份文件
    """
    try:
        # 读取文件
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 如果需要备份，创建备份文件
        if backup:
            backup_path = file_path.with_suffix(file_path.suffix + '.bak')
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Created backup file: {backup_path}")
            
        # 处理内容
        new_content = wrap_badges_with_div(content, div_classes)
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"Successfully processed {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")

def main():
    # 创建参数解析器
    parser = argparse.ArgumentParser(
        description='处理 Markdown 文件，将连续的 badge 行包装在 div 标签中。',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例：
  %(prog)s file.md                    # 处理单个文件
  %(prog)s file1.md file2.md          # 处理多个文件
  %(prog)s -b file.md                 # 创建备份后处理
  %(prog)s -c "custom-class" file.md  # 使用自定义类名
        """
    )
    
    # 添加参数
    parser.add_argument('files', nargs='+', type=Path,
                        help='要处理的 Markdown 文件路径')
    parser.add_argument('-b', '--backup', action='store_true',
                        help='处理前创建备份文件（.md.bak）')
    parser.add_argument('-c', '--classes',
                        default="img-div hx-mt-4 hx-flex-row hx-justify-start hx-items-center",
                        help='div 标签的类名 (默认："img-div hx-mt-4 hx-flex-row hx-justify-start hx-items-center")')
    
    # 解析参数
    args = parser.parse_args()
    
    # 处理每个文件
    for file_path in args.files:
        if not file_path.exists():
            print(f"错误：文件不存在：{file_path}")
            continue
        if not file_path.is_file():
            print(f"错误：不是文件：{file_path}")
            continue
            
        process_file(file_path, args.classes, args.backup)

if __name__ == "__main__":
    main()
