#! /bin/bash

set -eux

django-admin compilemessages -l=ja
django-admin makemessages -l=ja
