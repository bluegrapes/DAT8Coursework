# DAT8Coursework

This repo contains the homeworks and project assignments for General Assembly Data Science Course, DAT8


#### tips for removing large files
git filter-branch --prune-empty --index-filter 'git rm -rf --cached --ignore-unmatch MY-BIG-DIRECTORY-OR-FILE' --tag-name-filter cat -- --all
