#!/bin/bash
# 起始页
page=1

# 用于保存输出的 JSON 文件
output_file="repos.json"

# 清空输出文件，确保每次运行时是从空文件开始
true >"$output_file"

# 循环直到获取所有页面的仓库名
while true; do
    # 发起请求，获取当前页的仓库
    response=$(curl -s -H "Authorization: token $TOKEN" \
        -H "Accept: application/vnd.github.v3+json" \
        "https://api.github.com/orgs/HITSZ-OpenAuto/repos?type=public&per_page=50&page=$page")

    # 将响应内容追加到文件中
    echo "$response" >>"$output_file"

    # 检查响应头中的 Link 是否包含 rel="next"，来判断是否有下一页
    header=$(curl -s -I -H "Authorization: token $TOKEN" \
        -H "Accept: application/vnd.github.v3+json" \
        "https://api.github.com/orgs/HITSZ-OpenAuto/repos?type=public&per_page=50&page=$page")

    set +e
    next_page=$(echo -e "$header" | grep -i 'rel="next"')
    set -e

    echo "$next_page"
    if [ -z "$next_page" ]; then
        break
    fi

    # 如果有下一页，增加页码
    page=$((page + 1))
done

echo "All public repositories have been saved to $output_file"
