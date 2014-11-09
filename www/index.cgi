#!/bin/sh

if [[ "$QUERY_STRING" =~ phpinfo ]]; then
	export PHPINFO_FILE=${RANDOM}_PHPINFO_TEMP.php
	echo "<?php phpinfo();unlink('${PHPINFO_FILE}'); ?>" > ${PHPINFO_FILE}
	echo "Location: ./${PHPINFO_FILE}

<a href='${PHPINFO_FILE}'>Click to visit ${PHPINFO_FILE}</a>"
	exit
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

if [ -f $RUNTIME_DIR/bin/php-cgi ]; then
	echo "Start coding or test <a href=\"?phpinfo\">phpinfo</a>"
elif [ `ps aux|grep make.sh|wc -l` != 0 ]; then
	echo "Still preparing..."
else
	echo "Run <u>nohup \${OPENSHIFT_REPO_DIR}/misc/make.sh &amp;</u> and start waiting. You can refresh this page to get newest status."
fi

echo "</p></body></html>"