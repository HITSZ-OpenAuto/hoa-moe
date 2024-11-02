# for every .md file in the content directory and its subdirectories, run the wrap.py script

# find all .md files in the content directory and its subdirectories
for file in $(find content/docs -name "*.md")
do
    # run the wrap.py script on each file
    python scripts/wrap_badges.py $file
done
