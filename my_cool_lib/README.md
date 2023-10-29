

# Create release
```shell
rm -rf dist
poetry build
gh release delete v$(poetry version -s) -y
gh release create v$(poetry version -s) dist/*.tar.gz --generate-notes
```