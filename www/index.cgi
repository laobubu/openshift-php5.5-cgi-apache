#!/bin/bash

if [[ "$QUERY_STRING" =~ "phpinfo" ]]; then
	export PHPINFO_FILE=${RANDOM}_PHPINFO_TEMP.php
	echo "<?php phpinfo();unlink('${PHPINFO_FILE}'); ?>" > ${PHPINFO_FILE}
	echo "Location: ./${PHPINFO_FILE}

<a href='${PHPINFO_FILE}'>Click to visit ${PHPINFO_FILE}</a>"
	exit
fi

if [[ "$QUERY_STRING" =~ "doitnow" ]]; then
	chmod +x ${OPENSHIFT_REPO_DIR}/misc/make.sh
	nohup ${OPENSHIFT_REPO_DIR}/misc/make.sh > /tmp/makephp &
	sleep 1
	echo "Location: ./?working

<a href='./?working'>Click to refresh</a>"
fi

cd ../..
export RUNTIME_DIR=${PWD}

echo "Content-Type: text/html
X-Powered-By: /bin/bash

<html>
<head>
<title>Installed</title>
</head>
<body>
<h1>Installed</h1>
<p>You just created one amazing PHP5.5+Apache app.</p>
<h2>Next...</h2>
<p>"

if [[ -x ${OPENSHIFT_RUNTIME_DIR}/bin/php-cgi ]]; then
	echo "Start coding or test <a href=\"?phpinfo\">phpinfo</a>. <b>Remember to remove index.cgi</b>"
elif [[ -f /tmp/makephp ]]; then
	echo "<p>Still spawning your world...</p>"
	echo "<p>This page shall refresh automatically...</p>"
	echo "<p>Now you can close this page, and come back whenever...</p>"
	echo "<p>Have problem? <a href=https://github.com/laobubu/openshift-php5.5-cgi-apache/issues/new >submit issue.</a></p>"
	echo "<div style='font-size:.7em;font-family:Courier'>"
	tail /tmp/makephp
	echo "</div>"
	echo "<script>setTimeout(function(){window.location.reload(true)},10000)</script>"
else
	echo "<p>Follow the instruction on <a href=https://github.com/laobubu/openshift-php5.5-cgi-apache>https://github.com/laobubu/openshift-php5.5-cgi-apache</a>."
	echo "<p>You can refresh this page to check if the world is ready."
	echo "<p><a href=?doitnow>Come on, robot, you can do it automatically...</a><p>"
fi

echo "</p></body></html>"