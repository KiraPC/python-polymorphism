rm -rf .eggs/
rm -rf python_polymorphism.egg-info/
rm -rf dist/

git pull

python setup.py sdist
twine upload dist/*