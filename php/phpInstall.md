install.md  
New CakePHP 3.4 Red Velvet.
http://windows.php.net/download#php-5.6-ts-VC11-x64  
[download php from here](http://windows.php.net/download)  
[php-5.3.3-Win32-VC9-x86:download php from here](http://windows.php.net/downloads/releases/archives/)  
[apache2.2final](https://www.apachehaus.com/cgi-bin/download.plx#APACHE22VC09)
(http://www.microsoft.com/downloads/en/details.aspx?FamilyID=A5C84275-3B97-4AB7-A40D-3802B2AF5FC2)
[download composer here](https://getcomposer.org/download/)  

###### in .bash_profile
```
export HTTP_PROXY_REQUEST_FULLURI=true
export HTTPS_PROXY_REQUEST_FULLURI=false
```
###### composer
```
php composer.phar self-update
composer.phar update
curl -v https://getcomposer.org/version
php composer.phar diag
curl https://getcomposer.org/installer > composer-setup.php
php composer-setup.php
install composer.exe
```

###### wget download_url
```
wget http://ftp.tu-chemnitz.de/pub/linux/dag/redhat/el6/en/i386/rpmforge/RPMS/judy-1.0.5-1.el6.rf.i686.rpm
```
###### Judy
```
yum -y install http://ftp.tu-chemnitz.de/pub/linux/dag/redhat/el6/en/i386/rpmforge/RPMS/rpmforge-release-0.5.2-1.el6.rf.i686.rpm
yum -y install http://ftp.tu-chemnitz.de/pub/linux/dag/redhat/el6/en/i386/rpmforge/RPMS/rpmforge-release-0.5.2-2.el6.rf.i686.rpm
yum -y install http://ftp.tu-chemnitz.de/pub/linux/dag/redhat/el6/en/i386/rpmforge/RPMS/rpmforge-release-0.5.3-1.el6.rf.i686.rpm
sudo pecl -d preferred_state=beta install Judy
```
##### memprof
```
sudo pecl install memprof-1.0.0
```
###### intl.so
```
pecl install intl
xcode-select --install 
php -i | grep php.ini
php -i | grep intl
php -m  #list php modules installed.
```
 [pear_install_guide](https://jason.pureconcepts.net/2012/10/install-pear-pecl-mac-os-x/)

###### config settings
```
create php.ini from php.ini-development;
in php.ini, enable openssl,extension_dir,php_intl,mbstring,sqlite,mysql;
extension_dir = "ext"
intl.default_locale =en_utf8
mbstring.language = Japanese

set php path to env var;
```
###### for test:
https://github.com/cakephp/cakephp
```
composer create-project --prefer-dist cakephp/app cakeapp
php composer.phar create-project --prefer-dist cakephp/app cakeapp
php composer.phar create-project --prefer-dist cakephp/app cakeapp
```
Installing cakephp/app (3.4.2)
```
chmode +x cake

bin/cake server -p 8765
.\bin\cake server -p 8765
http://localhost:8765
bin/cake server -p 8080
http://localhost:8080
```
http_proxy:
disable local proxy.

[xdebug](https://xdebug.org/download.php)

###### show all info for php
phpinfo();

[http install](http://www.jp.t2softworks.com/php/s401.htm)  

#### to enable httpd connect db
sudo setsebool -P httpd_can_network_connect_db 1  
sudo getsebool httpd_can_network_connect_db  
#### to enable httpd write logs
chown -R apache:apache /var/www/html/cake/app/tmp/*  
#### code sniffer
```
pear install PHP_CodeSniffer-2.9.1
```
#### install php7
```
yum install epel-release
rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm
yum install --enablerepo=remi,remi-php70 php php-devel php-mbstring php-pdo php-gd php-xml php-mcrypt
yum install --enablerepo=remi,remi-php70 php-pgsql
yum install --enablerepo=remi,remi-php70 php-mysql
yum install --enablerepo=remi,remi-php70 php-pear
pecl install Xdebug

rpm -qa | grep php
yum remove php-*

php -v
PHP 7.0.28 (cli) (built: Feb 27 2018 16:07:52) ( NTS )
```
