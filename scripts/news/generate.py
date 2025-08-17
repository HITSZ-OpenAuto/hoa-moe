import os
import logging
from openai import OpenAI
import base64

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url="https://api.aihubmix.com/v1/",
)


def generate_image(prompt):
    """Generate a random image of abstract art using DALL-E."""
    logger.info("Generating the cover image...")
    prompt = prompt

    result = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1024"
    )

    image_base64 = result.data[0].b64_json
    image_bytes = base64.b64decode(image_base64)

    # Save the image to a file
    with open("generated_image.png", "wb") as f:
        f.write(image_bytes)
        print("Image downloaded and saved as 'generated_image.png'")


def generate_summary(raw_updates):
    """Generate a summary using OpenAI's API."""
    logger.info("Generating AI summary...")
    prompt = f"""你将收到一周内学生们在各个课程仓库中的更新记录。  
请根据这些原始更新，生成一个简洁清晰的「每周更新摘要」，要求如下：  

1. 按照课程进行归类，不需要逐日分开。  
2. 同一门课程的多条类似更新请合并，避免重复啰嗦。  
3. 重点突出：
   - 新增的资料、作业、代码、讲义、教材、试卷等。
   - 对课程说明/文档的重要修改。
   - 有价值的合并更新（如 OpenCS 内容）。  
4. 对琐碎操作（如删除无意义的 README、文件改名、格式小改）只需一句话笼统概括。  
5. **如果一周内仅有一个仓库更新，请直接输出 `__NO_SUMMARY__`，不要生成摘要。**  
6. 输出风格应简洁明了，适合在新闻模块展示。  

下面是原始更新内容：  

{raw_updates}

请生成总结。"""
    try:
        summary = client.responses.create(
            model="gpt-5-mini",
            input=prompt
        )
        return summary.output_text
    except Exception:
        logger.error("Error generating AI summary", exc_info=True)
        return None
