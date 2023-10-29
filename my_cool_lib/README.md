

# Install package
```shell
pip install git+https://github.com/Slamnlc/pytest_plugin_demo.git#subdirectory=my_cool_lib
```


# Create release on GitHub (optional)
```shell
rm -rf dist
poetry build
gh release delete v$(poetry version -s) -y
gh release create v$(poetry version -s) dist/*.tar.gz --generate-notes
```