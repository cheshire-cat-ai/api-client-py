docker run --rm -v "${PWD}":/local openapitools/openapi-generator-cli generate \
-i /local/openapi.json \
 -g python \
  --git-host github.com \
  --git-repo-id api-client-py \
  --git-user-id cheshire-cat-ai \
  --package-name cheshire_cat_api \
  -o /local/.