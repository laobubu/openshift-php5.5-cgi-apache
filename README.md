# PHP5.5 + Apache 

This modified DIY cartridge provides PHP 5.5.31 and fully free Apache configuration permission, which can be found in `conf` folder.

## Quick Start

[![Click to install OpenShift](http://launch-shifter.rhcloud.com/launch/light/Click to install.svg)](https://openshift.redhat.com/app/console/application_type/custom?&cartridges[]=diy-0.1&initial_git_url=https://github.com/laobubu/openshift-php5.5-cgi-apache.git&name=php)

1. Open https://openshift.redhat.com/app/console/application_type/cart!diy-0.1 
2. Fill **Source Code** text field: `https://github.com/laobubu/openshift-php5.5-cgi-apache.git`
3. Click **Create Application** and wait
4. Open your website (e.g. foo-bar.rhcloud.com ) and keep your browser running. Meanwhile, you can `git clone` your app to your computer and start coding.
5. **IMPORTANT** : your first `git push` shall NOT be earlier than the first building ends

### Tips

* The first building lasts for ~20 minutes, the progress can be seen on your app page (eg. https://foo-bar.rhcloud.com )
* By default, PHP 5.5.31 is choosen, which can be found in `misc/make.sh`
* Once you modified `conf/httpd.conf`, you must reload your app, or run `${OPENSHIFT_REPO_DIR}/.openshift/action_hooks/reload`, to make it works.
* If you are using Windows, please follow the Quick Start instruction!!!
* The OpenShift `diy` cartridge documentation can be found at:
http://openshift.github.io/documentation/oo_cartridge_guide.html#diy
