git add .
git commit -m "update"
git push

Викласти сайт онлайн:
mkdocs gh-deploy

## видалити файл безслідно
pip install git-filter-repo
git filter-repo --path --force docs/help.md --invert-paths

git remote add origin https://github.com/USERNAME/embedded-notes.git
git remote -v

git push origin main --force
git push origin gh-pages --force
