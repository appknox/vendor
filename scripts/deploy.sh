#! /bin/bash
#
# deploy.sh
# Copyright (C) 2015 dhilipsiva <dhilipsiva@gmail.com>
#
# Distributed under terms of the MIT license.
#


rm -rf dist/
poetry version patch
export CURRENT_BRANCH
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
VERSION=$(poetry version -s)
git commit -am "Version bump $VERSION"
git push origin "$CURRENT_BRANCH:$CURRENT_BRANCH"
poetry publish --build
