# PHP5.5 + Apache 

This modified DIY cartridge provides newer PHP and freer Apache configuration, which can be found in `conf/httpd.conf` folder.

## Quick Start
1. Push this repo to your OpenShift.
2. Access SSH and Run `nohup ${OPENSHIFT_REPO_DIR}/misc/make.sh &` to make your own PHP5.5.
3. Give your family/friend a ring or watch a movie.
4. Do what you want.

### Tips
* You can also choose other version of PHP by editing `misc/make.sh` before making.
* Once you modified `conf/httpd.conf`, you must reload your app, or run `${OPENSHIFT_REPO_DIR}/.openshift/action_hooks/reload`, to make it works.
* The OpenShift `diy` cartridge documentation can be found at:
http://openshift.github.io/documentation/oo_cartridge_guide.html#diy
