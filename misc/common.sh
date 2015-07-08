#!/bin/bash

export HTTPD_ARGUMENT="-f ${OPENSHIFT_REPO_DIR}/conf/httpd.conf"

export OPENSHIFT_RUNTIME_DIR=${OPENSHIFT_HOMEDIR}/app-root/runtime

env|>${OPENSHIFT_TMP_DIR}/httpd_temp.conf awk 'BEGIN{FS="="} $1 ~ /^OPENSHIFT/ {print "PassEnv", $1}'