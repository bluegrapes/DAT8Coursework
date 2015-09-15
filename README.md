# DAT8Coursework


# tips for removing large files
git filter-branch --prune-empty --index-filter 'git rm -rf --cached --ignore-unmatch MY-BIG-DIRECTORY-OR-FILE' --tag-name-filter cat -- --all
