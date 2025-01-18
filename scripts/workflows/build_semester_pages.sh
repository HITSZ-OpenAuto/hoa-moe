#!/bin/bash
semester_arr=('fresh-autumn' 'fresh-spring' 'fresh-summer' 'sophomore-autumn' 'sophomore-spring' 'sophomore-summer' 'junior-autumn' 'junior-spring' 'junior-summer' 'senior-autumn' 'senior-spring' 'graduate-autumn' 'graduate-spring' 'cross-specialty' 'general-knowledge')
category_arr='mandatory distributional-selective cross-major-selective graduate-course undergraduate-graduate-course selective general-knowledge legacy'

for ((i = 0; i < ${#semester_arr[@]}; i++)); do
    SEMESTER="${semester_arr[i]}"
    for CATEGORY in $category_arr; do
        if test -s "${SEMESTER}-${CATEGORY}.txt"; then
            cat "${SEMESTER}-${CATEGORY}.txt" >>"./content/docs/${SEMESTER}/_index.zh-cn.md"
            echo "{{< /cards >}}" >>"./content/docs/${SEMESTER}/_index.zh-cn.md"
        fi
    done
done
