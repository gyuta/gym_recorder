rm -f -r gym_record.egg-info/* dist/*
python setup.py sdist bdist_wheel
twine upload --repository pypi dist/*