#! /bin/bash
#
# deploy.sh
# Copyright (C) 2023 Appknox <engineering@appknox.com>
#
# Distributed under terms of the MIT license.
#

in_array() {
    local haystack="${1}[@]"
    local needle=${2}
    for i in ${!haystack}; do
        if [[ ${i} == "${needle}" ]]; then
            return 0
        fi
    done
    return 1
}

# shellcheck disable=SC2034
declare -a peotryversionpartarray=("major" "minor" "patch");

if in_array peotryversionpartarray "$1"; then
    echo "poetry version: $1"
else
    echo "ERROR: version is not one of major, minor, patch"
    exit 1
fi

echo "Creating release"
rm -rf dist/
poetry version "$1"
poetry update
export CURRENT_BRANCH
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
VERSION=$(poetry version -s)
git commit -am "Version bump $VERSION"
git push origin "$CURRENT_BRANCH:$CURRENT_BRANCH"
poetry publish --build
