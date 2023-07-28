#!/bin/bash

set -e

TAG=$(python -c 'import toml; t=toml.load("../pyproject.toml"); print(t["tool"]["poetry"]["version"])')

read -p "Creating new release for $TAG. Do you want to continue? [Y/n] " prompt

if [[ $prompt == "y" || $prompt == "Y" || $prompt == "yes" || $prompt == "Yes" ]]; then
#    python scripts/prepare_changelog.py
    git add -A
    git commit -m "Bump version to $TAG for release" || true && git push
    echo "Creating new git tag $TAG"
    git tag "$TAG" -m "$TAG"
    git-release "$TAG"
else
    echo "Cancelled"
    exit 1
fi

# Command to delete all local tags
# git tag | xargs git tag -d