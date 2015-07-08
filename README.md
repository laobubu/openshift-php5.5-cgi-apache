# PHP5.5 + Apache 

This modified DIY cartridge provides newer PHP and freer Apache configuration, which can be found in `conf/httpd.conf` folder.

## Quick Start

### Easiest Way

1. Open https://openshift.redhat.com/app/console/application_type/cart!diy-0.1 
2. Fill **Source Code** text field: `https://github.com/laobubu/openshift-php5.5-cgi-apache.git`
3. Click **Create Application** and wait
4. After creating the app, visit your app (e.g. https://foo-bar.rhcloud.com/ )
5. Click the last link.
6. Wait for ~1 hour and then PHP will be ready.
7. Git clone your OpenShift App and modify.

### Cool Way

1. Push the content of this repo to your OpenShift. *(Read Tips if you are using Windows)*
2. Access your app's URL like https://foo-bar.rhcloud.com
3. Click the Link.
4. Wait (Yes! It's slow!!!) , or do anything you want.

### Old School

1. Push the content of this repo to your OpenShift. *(Read Tips if you are using Windows)*
2. Access SSH and Run `chmod +x ${OPENSHIFT_REPO_DIR}/misc/make.sh && nohup ${OPENSHIFT_REPO_DIR}/misc/make.sh > /tmp/makephp&`
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
