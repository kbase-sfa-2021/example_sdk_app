#!/bin/bash
if [ -z "$GITHUB_ACTION" ]; then
  echo This script should only be run as a github action.
  exit 1;
fi

# This script is meant to be run once immediately after cloning this repo.
set -e
set -x

# TODO: Infer app name from directory.
name=$(basename "$(pwd)")

FILES=$(cat << HEREDOC
Makefile
RELEASE_NOTES.md
deploy.cfg
example_kb_sdk_app.spec
kbase.yml
lib/example_kb_sdk_app/example_kb_sdk_appImpl.py
lib/example_kb_sdk_app/example_kb_sdk_appServer.py
scripts/run_async.sh
test/example_kb_sdk_app_server_test.py
test/unit_tests/test_example_kb_sdk_app_utils.py
tox.ini
ui/narrative/methods/run_example_kb_sdk_app/spec.json
HEREDOC
)

for file in $FILES
do
    sed -i'.bak' "s/example_kb_sdk_app/${name}/g" "${file}"
done

git add -u

git mv example_kb_sdk_app.spec "${name}".spec
git mv lib/example_kb_sdk_app/example_kb_sdk_appImpl.py lib/example_kb_sdk_app/"${name}"Impl.py
git mv lib/example_kb_sdk_app/example_kb_sdk_appServer.py lib/example_kb_sdk_app/"${name}"Server.py
git mv lib/example_kb_sdk_app lib/"${name}"
git mv test/example_kb_sdk_app_server_test.py test/"${name}"_server_test.py
git mv test/unit_tests/test_example_kb_sdk_app_utils.py test/unit_tests/test_"${name}"_utils.py
git mv ui/narrative/methods/run_example_kb_sdk_app ui/narrative/methods/run_"${name}"

echo "# ${name}" > README.md

git add --update
OLD_GIT_USER_EMAIL=$(git config --get user.email)
OLD_GIT_USER_NAME=$(git config --get user.name)
git config user.email "KBase@example.com"
git config user.name "KBase"

# Delete this script
git rm -- "$0"

git commit --message="Renaming example module to ${name}."
if [ "$OLD_GIT_USER_EMAIL" ]; then
  git config user.email "$OLD_GIT_USER_EMAIL"
  git config user.name "$OLD_GIT_USER_NAME"
fi
