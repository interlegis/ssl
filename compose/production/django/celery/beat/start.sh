#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset


celery -A ssl.taskapp beat -l INFO
