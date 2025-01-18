#!/bin/bash
echo 'Checked. Start building.'
line="$REPO_NAME"
first_time=1

curl "https://raw.githubusercontent.com/HITSZ-OpenAuto/${line}/main/tag.txt" -o "tag_${line}.txt"
curl "https://raw.githubusercontent.com/HITSZ-OpenAuto/${line}/main/README.md" -o "temp.md"
python scripts/courses/gen_repo_update_time.py HITSZ-OpenAuto "${line}" "$TOKEN"
cp result_update_time_"${line}".txt result_time.txt
python scripts/courses/gen_links.py HITSZ-OpenAuto "$TOKEN"
# cp result.txt result_links.txt

Semesters=$(grep -E "^semester:..*$" "tag_${line}.txt")
Semesters=${Semesters#*: }

IFS=' / ' read -r -a semesters <<<"$Semesters"

for match_semester in "${semesters[@]}"; do
    case ${match_semester} in
    '第一学年秋季')
        semester='fresh-autumn'
        ;;
    '第一学年春季')
        semester='fresh-spring'
        ;;
    '第一学年夏季')
        semester='fresh-summer'
        ;;
    '第二学年秋季')
        semester='sophomore-autumn'
        ;;
    '第二学年春季')
        semester='sophomore-spring'
        ;;
    '第二学年夏季')
        semester='sophomore-summer'
        ;;
    '第三学年秋季')
        semester='junior-autumn'
        ;;
    '第三学年春季')
        semester='junior-spring'
        ;;
    '第三学年夏季')
        semester='junior-summer'
        ;;
    '第四学年秋季')
        semester='senior-autumn'
        ;;
    '第四学年春季')
        semester='senior-spring'
        ;;
    '研究生秋季')
        semester='graduate-autumn'
        ;;
    '研究生春季')
        semester='graduate-spring'
        ;;
    *)
        echo "No match semester"
        continue
        ;;
    esac

    CATEGORY=$(grep -E "^category:..*$" "tag_${line}.txt" | sed -E 's/^category:.(.*)$/\1/')

    # 针对文理通识和跨专业选修做的适配
    case ${CATEGORY} in
    '跨专业选修')
        semester='cross-specialty'
        ;;
    '文理通识')
        semester='general-knowledge'
        ;;
    *)
        echo "No match special categories"
        ;;
    esac

    if [ "$first_time" -eq 1 ]; then
        curl "https://raw.githubusercontent.com/HITSZ-OpenAuto/hoa-moe/main/content/docs/${semester}/${line}.md" -o "temp1.md"
        first_time=0
    fi

    head -n 7 "temp1.md" >"./content/docs/${semester}/${line}.md"

    {
        echo
        cat result_time.txt
        tail -n +2 "temp.md"
        echo
        echo "## 资料下载"
        echo
        cat scripts/infos/netdisk_notice.txt
        echo
        cat "${line}_cards.txt"
        echo
        cat scripts/infos/sponsor.txt
        echo
    } >>"./content/docs/${semester}/${line}.md"

    python scripts/courses/wrap_badges.py "content/docs/${semester}/${line}.md"
done
