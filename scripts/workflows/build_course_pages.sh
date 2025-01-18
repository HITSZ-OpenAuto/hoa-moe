#!/bin/bash
# 建立课程页面
counter_man=0
counter_dis=100
counter_graduate=200
counter_cross=300
counter_general=400
counter_legacy=1000
for line in $(echo "$REPOS_ARRAY" | jq -r '.[]'); do
    set +e
    echo "$line" | grep -qE '^([A-Z]{2,4}[0-9]{3}([0-9]|X){1}|MOOC|GeneralKnowledge|CrossSpecialty).*$'
    if [ $? -eq 1 ]; then
        continue
    fi
    set -e
    echo '-------------------------------------------------'
    echo "${line}"
    curl "https://raw.githubusercontent.com/HITSZ-OpenAuto/${line}/main/tag.txt" -o "tag_${line}.txt"

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

        echo "$semester"

        CATEGORY=$(grep -E "^category:..*$" "tag_${line}.txt" | sed -E 's/^category:.(.*)$/\1/')

        case ${CATEGORY} in
        '必修')
            category='mandatory'
            ;;
        '限选')
            category='distributional-selective'
            ;;
        '研究生阶段课程')
            category='graduate-course'
            ;;
        '本研共通')
            category='undergraduate-graduate-course'
            ;;
        '选修')
            category='selective'
            ;;
        '跨专业选修')
            semester='cross-specialty'
            category='cross-major-selective'
            ;;
        '文理通识')
            semester='general-knowledge'
            category='general-knowledge'
            ;;
        '归档')
            category='legacy'
            ;;
        *)
            echo "No match category"
            continue
            ;;
        esac

        echo "$category"

        grep -E "^name:..*$" "tag_${line}.txt" | sed -E 's/^name:.(.*)$/\1/' >"name_${line}.txt"

        if test ! -s "${semester}-${category}.txt"; then
            if [ "${CATEGORY}" = "必修" ]; then
                echo "## ${CATEGORY}" >"${semester}-${category}.txt"
            fi
            if [ "${CATEGORY}" = "限选" ]; then
                echo "## ${CATEGORY}" >"${semester}-${category}.txt"
                echo "[限选课选课指南](https://hoa.moe/blog/distributive-guidance-for-22/)" >>"${semester}-${category}.txt"
            fi
            # if [ ${CATEGORY} = "跨专业选修" ]
            # then
            #   echo "[查看跨专业选修课选课指南](https://hoa.moe/blog/selecting-cross-major-lessons/)" >> "${semester}-${category}.txt"
            # fi
            if [ "${CATEGORY}" = "研究生阶段课程" ]; then
                echo "## ${CATEGORY}" >"${semester}-${category}.txt"
                echo "此类课程是本科生可跨选的研究生阶段课程。它们也属限选课，但是与专业限选课性质不同，故单独列出。具体请看[研究生阶段课程选课指南](https://hoa.moe/blog/master-phd-course-selection/)。" >>"${semester}-${category}.txt"
            fi
            if [ "${CATEGORY}" = "本研共通" ]; then
                echo "## ${CATEGORY}" >"${semester}-${category}.txt"
                echo "此类课程是本科生可跨选的研究生阶段课程。它们也属限选课，但是与专业限选课性质不同，故单独列出。具体请看[研究生阶段课程选课指南](https://hoa.moe/blog/master-phd-course-selection/)。" >>"${semester}-${category}.txt"
            fi
            if [ "${CATEGORY}" = "选修" ]; then
                echo "## ${CATEGORY}" >"${semester}-${category}.txt"
            fi
            if [ "${CATEGORY}" = "归档" ]; then
                echo "## ${CATEGORY}" >"${semester}-${category}.txt"
                echo "此类课程在之前的培养方案中处于较重要的地位，但由于培养方案的调整，现在不再开设了。不过，原课程资料仍保留，感兴趣的同学可以自行查阅。" >>"${semester}-${category}.txt"
            fi
            echo "<!--more-->" >>"${semester}-${category}.txt"
            echo "{{< cards >}}" >>"${semester}-${category}.txt"
        fi

        echo -n "{{< card link=\"${line}\"" | tr '[:upper:]' '[:lower:]' >>"${semester}-${category}.txt"
        echo "title=\"$(cat "name_${line}.txt")\">}}" >>"${semester}-${category}.txt"

        echo '------index.txt-------'
        cat "${semester}-${category}.txt"
        echo '----------------------'

        echo '---' >"./content/docs/${semester}/${line}.md"
        if [ "${CATEGORY}" = "跨专业选修" ] || [ "${CATEGORY}" = "文理通识" ]; then
            echo "title: $(cat "name_${line}.txt")" >>"./content/docs/${semester}/${line}.md"
        else
            echo "title: （${CATEGORY}）$(cat "name_${line}.txt")" >>"./content/docs/${semester}/${line}.md"
        fi

        case "${CATEGORY}" in
        "必修")
            counter_man=$((counter_man + 1))
            echo "weight: $counter_man" >>"./content/docs/${semester}/${line}.md"
            ;;
        "限选")
            counter_dis=$((counter_dis + 1))
            echo "weight: $counter_dis" >>"./content/docs/${semester}/${line}.md"
            ;;
        "研究生阶段课程" | "本研共通" | "选修")
            counter_graduate=$((counter_graduate + 1))
            echo "weight: $counter_graduate" >>"./content/docs/${semester}/${line}.md"
            ;;
        "跨专业选修")
            counter_cross=$((counter_cross + 1))
            echo "weight: $counter_cross" >>"./content/docs/${semester}/${line}.md"
            ;;
        "文理通识")
            counter_general=$((counter_general + 1))
            echo "weight: $counter_general" >>"./content/docs/${semester}/${line}.md"
            ;;
        "归档")
            counter_legacy=$((counter_legacy + 1))
            echo "weight: $counter_legacy" >>"./content/docs/${semester}/${line}.md"
            ;;
        esac

        {
            echo 'toc: true'
            echo "editURL: \"https://github.com/HITSZ-OpenAuto/${line}/edit/main/README.md\""
            echo "math: true"
            echo '---'
            echo
        } >>"./content/docs/${semester}/${line}.md"

        python scripts/courses/gen_repo_update_time.py HITSZ-OpenAuto "${line}" "$TOKEN"

        {
            cat result_update_time_"${line}".txt
            curl -s "https://raw.githubusercontent.com/HITSZ-OpenAuto/${line}/main/README.md" -o "temp.md"
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
    done
done
