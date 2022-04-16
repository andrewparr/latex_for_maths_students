#!/usr/bin/env bash
set -e

make clean html

rm -rf deploy
git clone https://github.com/andrewparr/latex_for_maths_students.git deploy
cd deploy
git checkout gh-pages
rm -rf * .gitignore .buildinfo .nojekyll
cp -r ../build/html/./ .
touch .nojekyll
git add .
git commit -m "Update `date`"
git push origin gh-pages

cd ..
rm -rf deploy