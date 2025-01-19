#!/bin/bash
echo 'First check: file existence'
line="$REPO_NAME"
echo '-------------------------------------------------'
echo "${line}"
set +e
curl "https://raw.githubusercontent.com/HITSZ-OpenAuto/${line}/main/tag.txt" -o "tag_${line}.txt"
if [ $? -ne 0 ]; then
    echo "Error: tag file not found or connection failed"
    set -e
    exit 1
fi
set -e

echo " "
echo '-----tag.txt-----'
cat "tag_${line}.txt"
echo " "
echo '-----------------'

Semesters=$(grep -E "^semester:..*$" "tag_${line}.txt")
Semesters=${Semesters#*: }
echo "${Semesters}"

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

    echo "$semester"

    # Ensure the if statement can be executed
    set +e
    curl -sf -o /dev/null "https://raw.githubusercontent.com/HITSZ-OpenAuto/hoa-moe/main/content/docs/${semester}/${line}.md"
    if [ $? -ne 0 ]; then
        echo "Error: Course pages have not been created yet. "
        curl -X POST \
            -H "Accept: application/vnd.github.v3+json" \
            -H "Authorization: token $TOKEN" \
            https://api.github.com/repos/HITSZ-OpenAuto/hoa-moe/actions/workflows/course.yaml/dispatches \
            -d '{"ref":"main"}'
        set -e
        exit 1
    fi
    set -e
done
