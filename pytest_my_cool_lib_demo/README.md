# Install package from GitHub

```shell
pip install git+https://github.com/Slamnlc/pytest_plugin_demo.git#subdirectory=pytest_my_cool_lib_demo
```

# Upload to Pypi

```shell
poetry publish --build --username __token__ --password %YOUR_TOKEN%
```

# Create release on GitHub (optional)

```shell
rm -rf dist
poetry build
gh release delete v$(poetry version -s) -y
gh release create v$(poetry version -s) dist/*.tar.gz --generate-notes
```

# Update version

```shell
poetry version minor
```
