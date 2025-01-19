#!/bin/bash
semester_arr=('fresh-autumn' 'fresh-spring' 'fresh-summer' 'sophomore-autumn' 'sophomore-spring' 'sophomore-summer' 'junior-autumn' 'junior-spring' 'junior-summer' 'senior-autumn' 'senior-spring' 'graduate-autumn' 'graduate-spring' 'cross-specialty' 'general-knowledge')
semester_name=('大一·秋' '大一·春' '大一·夏' '大二·秋' '大二·春' '大二·夏' '大三·秋' '大三·春' '大三·夏' '大四·秋' '大四·春' '研究生·秋' '研究生·春' '跨专业选修' '文理通识与MOOC')
category_arr='mandatory distributional-selective cross-major-selective graduate-course undergraduate-graduate-course selective general-knowledge legacy'

for ((i = 0; i < ${#semester_arr[@]}; i++)); do
    SEMESTER="${semester_arr[i]}"
    OUT="${semester_name[i]}"
    INDEX_FILE="./content/docs/${SEMESTER}/_index.zh-cn.md"

    echo "Creating a folder for a new semester"
    mkdir -p "./content/docs/${SEMESTER}"
    echo "./content/docs/${SEMESTER}"
    echo '---' >"${INDEX_FILE}"
    {
        echo "title: ${OUT}"
        echo "weight: $((i + 2))"
        echo 'comments: false'
        echo 'toc: false'
        echo '---'
        echo "探索以下各节以查找相关资料"
    } >>"${INDEX_FILE}"
    for CATEGORY in $category_arr; do
        touch "${SEMESTER}-${CATEGORY}.txt"
    done
done

# echo "${{ steps.modified_files_list.outputs.stringList }}" > tmp.txt
# cat tmp.txt | grep -E "^-.(([A-Z]){2,4}([0-9]){3}([0-9]|X){1}|MOOC|GeneralKnowledge|CrossSpecialty).*$" | sed -E 's/^..(.*)$/\1/' > repos.txt
# cat repos.txt
