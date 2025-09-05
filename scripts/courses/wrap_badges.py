import re
import sys
import logging
from pathlib import Path
import urllib.parse

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def wrap_badges_with_div(content):
    """
    Find consecutive badge lines and wrap them with div

    Args:
        content (str): Content to process
    """
    custom_badge_class = "hoa-badge"
    lines = content.split("\n")
    processed_lines = []

    # Badge line regex pattern
    badge_pattern = r"!\[.*?\]\(<?https://img\.shields\.io/badge/[^)]+>?\)"

    i = 0
    while i < len(lines):
        if "<div class=" in lines[i]:
            logger.debug(f"Found existing div line: {lines[i]}")
            processed_lines.append(f'<div class="{custom_badge_class}">')
            i += 1

            while i < len(lines) and "</div>" not in lines[i]:
                line = lines[i]
                # Encode only the Chinese characters in the entire line
                line = re.sub(
                    badge_pattern,
                    lambda m: m.group(0).replace(
                        m.group(0),
                        re.sub(
                            r"([\u4e00-\u9fff]+)",
                            lambda c: urllib.parse.quote(c.group()),
                            m.group(0),
                        ),
                    ),
                    line,
                )

                processed_lines.append(line)
                i += 1
            if i < len(lines):
                processed_lines.append(lines[i])  # Add closing </div>
            i += 1
            continue
        if re.search(badge_pattern, lines[i]):
            logger.debug(f"Found badge line: {lines[i]}")
            # Find consecutive badge lines
            badge_block = []
            while i < len(lines) and (
                re.search(badge_pattern, lines[i]) or lines[i].strip() == ""
            ):
                line = lines[i]
                # Encode only the Chinese characters in the entire line
                line = re.sub(
                    badge_pattern,
                    lambda m: m.group(0).replace(
                        m.group(0),
                        re.sub(
                            r"([\u4e00-\u9fff]+)",
                            lambda c: urllib.parse.quote(c.group()),
                            m.group(0),
                        ),
                    ),
                    line,
                )
                badge_block.append(line)
                i += 1

            if badge_block:
                logger.debug("Wrapping badge block with div.")
                processed_lines.append(f'<div class="{custom_badge_class}">\n')
                processed_lines.extend(badge_block)
                processed_lines.append("</div>\n")
            else:
                logger.debug("No badge lines found in the block.")
        else:
            logger.debug(f"Found non-badge line: {lines[i]}")
            processed_lines.append(lines[i])
            i += 1

    return "\n".join(processed_lines)


def process_file(file_path):
    """
    Process the specified markdown file

    Args:
        file_path (Path): File path
    """
    try:
        # Read file
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Process content
        new_content = wrap_badges_with_div(content)

        # Write back to file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        logger.info(f"Successfully processed {file_path}")
    except Exception as e:
        logger.error(f"Error processing {file_path}: {str(e)}")


def main():
    file_path = Path(sys.argv[1])
    process_file(file_path)


if __name__ == "__main__":
    main()
