#!/bin/bash
#
# This is just a friendly notice page.
# Feel free to delete this file.
#

if [[ -x ${OPENSHIFT_HOMEDIR}/app-root/runtime/bin/php-cgi ]] ; then

	PHPINFO_FILE=${RANDOM}_PHPINFO_TEMP.php
	>${PHPINFO_FILE} echo "<?php phpinfo(); unlink('${PHPINFO_FILE}'); ?>"
    
    echo "Location: ./${PHPINFO_FILE}"
    echo "Content-Type: text/html"
    echo ""
    echo "<meta http-equiv=\"refresh\" content=\"0; url=${PHPINFO_FILE}\">"
    echo "leading you to the one-time phpinfo page <a href=\"${PHPINFO_FILE}\">${PHPINFO_FILE}</a>"
    
    rm -f ${OPENSHIFT_REPO_DIR}/www/index.cgi
    
    exit 0
fi

LOG_FILE=/tmp/build_log
PID_FILE=/tmp/build_pid

PID=` 2>/dev/null cat ${PID_FILE} `
MESSAGE=''

if [[ "$QUERY_STRING" =~ "force_stop" ]]; then
    kill -9 $PID
    rm -f $LOG_FILE $PID_FILE
    MESSAGE="build proc $PID killed."
fi


if [[ "$QUERY_STRING" =~ "doitnow" ]]; then
    >/dev/null nohup ${OPENSHIFT_REPO_DIR}/.openshift/action_hooks/build &
    sleep 1
    MESSAGE="build started. if last build is not stopped, it might fail."
fi

echo "Content-Type: text/html"
echo ""
cat << EOF

<h1> Hello PHP on OpenShift </h1>

<p> Your PHP environment is not ready yet, please wait...
<p> It will finish in half an hour.
<p> Do NOT update / restart / stop your OpenShift App before it finishes.
</p>
<h2> Links </h2>
<p> More Information: <a href='https://github.com/laobubu/openshift-php5.5-cgi-apache'>https://github.com/laobubu/openshift-php5.5-cgi-apache</a>
</p>
<h2> Control </h2>

    [ <a href="?full_log">   show full build log </a> ]
    [ <a href="?force_stop"> force stop building </a> ]
    [ <a href="?doitnow">    start building      </a> ]

<h2> Build Status </h2>
EOF

if [[ ! "$QUERY_STRING" =~ "full_log" ]]; then
    echo "<script>setTimeout(function(){location.href='?_t=' + +new Date()}, 10000)</script>"
    echo "<p>This page will refresh automatically to keep server awake. Do not close this page.</p>"
else
    echo "<p>Auto-refreshing is disabled. To keep server awake, please <a href=\"?_t=0\">go back</a></p>"
fi

[ "$MESSAGE" ] && echo "<b>$MESSAGE</b>"

echo "<pre>"

if [ ! -f $PID_FILE ] || [ ! "$PID" ] || [ ! -f /proc/${PID}/stat ]; then
    echo "<b>WARNING: BUILD PROCCESS MIGHT NOT RUNNING</b>"
else
    echo "<b>build pid = $PID </b>"
fi

if [ -f $LOG_FILE ]; then 
    ( [[ "$QUERY_STRING" =~ "full_log" ]] && cat $LOG_FILE || tail -n 25 $LOG_FILE ) | sed -e 's/\&/\&amp;/' -e 's/</\&lt;/'
fi

echo "</pre>"


exit 0
