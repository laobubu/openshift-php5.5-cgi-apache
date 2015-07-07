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
fi

cd ../..
export RUNTIME_DIR=${PWD}

echo "Content-Type: text/html
X-Powered-By: /bin/sh

<html>
<head>
<title>Installed</title>
</head>
<body>
<h1>Installed</h1>
<p>You just created one amazing PHP5.5+Apache app.</p>
<h2>Next...</h2>
<p>"

if [[ -x $OPENSHIFT_RUNTIME_DIR/bin/php-cgi ]]; then
	echo "Start coding or test <a href=\"?phpinfo\">phpinfo</a>"
elif [[ -f /tmp/makephp ]]; then
	echo "Still spawning your world..."
	echo "<pre>"
	tail /tmp/makephp
	echo "</pre>"
else
	echo "<p>Follow the instruction on <a href=https://github.com/laobubu/openshift-php5.5-cgi-apache>https://github.com/laobubu/openshift-php5.5-cgi-apache</a>."
	echo "<p>You can refresh this page to check if the world is ready."
	echo "<p><a href=?doitnow>I AM BUSY. DO IT NOW.</a><p>"
fi

echo "</p></body></html>"