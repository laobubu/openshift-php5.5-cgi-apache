# PHP5.5 + Apache 

This modified DIY cartridge provides newer PHP and freer Apache configuration, which can be found in `conf/httpd.conf` folder.

## Quick Start

### Cool Way

1. Push this repo to your OpenShift, without any change!
2. Access your app's URL like https://foo-bar.rhcloud.com
3. Click the Link.
4. Wait (Yes! It's slow!!!) , or do anything you want.

### Old School

1. Push this repo to your OpenShift.
2. Access SSH and Run the following command to make your own PHP5.5.
```
chmod +x ${OPENSHIFT_REPO_DIR}/misc/make.sh
nohup ${OPENSHIFT_REPO_DIR}/misc/make.sh > /tmp/makephp&
```
3. Give your family/friend a ring or watch a movie.
4. Do what you want.

### Tips

* You can also choose other version of PHP by editing `misc/make.sh` before making.
* Once you modified `conf/httpd.conf`, you must reload your app, or run `${OPENSHIFT_REPO_DIR}/.openshift/action_hooks/reload`, to make it works.
* If you are using Windows, the permission information might be lost. To avoid the problem, you can try this in Git Bash:
```
git clone https://github.com/laobubu/openshift-php5.5-cgi-apache.git --depth 1
cd openshift-php5.5-cgi-apache
git remote set-url origin ssh://xxxxxxxxxxx@foo-bar.rhcloud.com/xxxxxxx #replace this
git push origin -f
#since then, the repo is yours and do whatever you want.
```
* The OpenShift `diy` cartridge documentation can be found at:
http://openshift.github.io/documentation/oo_cartridge_guide.html#diy
