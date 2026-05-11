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

## переглянути файл
watchfiles --ignore-paths docs/site "python -m mkdocs build --dirty" docs

python -m mkdocs build --dirty

!!! tip Пояснення “як запам’ятати”

!!! danger Типові помилки студентів

!!! warning Важливі моменти

!!! info Довідкова інформація (пін, напруга, параметри)

!!! note Теорія

!!! question Контрольні питання

??? note "Детальніше про GPIO"
    Тут додаткове пояснення
    студент може розгортати/згортати

??? warning "Типова помилка"
    Не підключай LED без резистора