

Puppet Essentials for Beginners   (3 vm learning)
by Anirban Saha
Published: April 2017

install virtualbox  for windows
install git
Install  vagrant  
open  git-bash  on c:\bobtk
cd /c/bobtk/Anirbanpuppet/
vagrant version
vagrant init
## to make 1 centOS puppetMaster 1 centOS agent 1 ubuntu Agent 
vi Vagrantfile     
Vagrant.configure("2") do |config|
# make sure vm ips  different from LAN ips of other devicesa
	config.vm.define "puppetmaster" do |pm|
		pm.vm.box = "centos/7"
		pm.vm.network "private_network",ip: "192.168.2.161"
		pm.vm.hostname = "puppetmaster"
		pm.vm.provider "virtualbox" do |v-pm|
			v-pm.memory = 2500
			v-pm.cpus = 2
		end
	end
	config.vm.define "puppet-agent-centos" do |pac|
		pac.vm.box = "centos/7"
		pac.vm.network "private_network",ip: "192.168.2.162"
		pac.vm.hostname = "centos-agent"
		pac.vm.provider "virtualbox" do |v-pac|
			v-pac.memory = 1800
			v-pac.cpus = 1
		end		 
	end
	config.vm.define "puppet-agent-ubuntu" do |pau|
		pau.vm.box = "ubuntu/xenial64"
		pau.vm.network "private_network",ip: "192.168.2.163"
		pau.vm.hostname = "ubuntu-agent"
		pac.vm.provider "virtualbox" do |v-pau|
			v-pau.memory = 1750
			v-pau.cpus = 1
		end		 
	end
end

# if want to make  1 centOS puppetMaster 2 centOS agents use below vagrant file configuration   
vi Vagrantfile     
Vagrant.configure("2") do |config|
# make sure vm ips  different from LAN ips of other devicesa
	config.vm.define "puppetmaster" do |pm|
		pm.vm.box = "centos/7"
		pm.vm.network "private_network",ip: "192.168.2.161"
		pm.vm.hostname = "puppetmaster"
		pm.vm.provider "virtualbox" do |v-pm|
			v-pm.memory = 2500
			v-pm.cpus = 2
		end
	end
	config.vm.define "puppet-agent-centos1" do |pac|
		pac.vm.box = "centos/7"
		pac.vm.network "private_network",ip: "192.168.2.162"
		pac.vm.hostname = "centos-agent"
		pac.vm.provider "virtualbox" do |v-pac|
			v-pac.memory = 1800
			v-pac.cpus = 1
		end		 
	end
	config.vm.define "puppet-agent-centos2" do |pac|
		pac.vm.box = "centos/7"
		pac.vm.network "private_network",ip: "192.168.2.163"
		pac.vm.hostname = "centos-agent"
		pac.vm.provider "virtualbox" do |v-pac|
			v-pac.memory = 1800
			v-pac.cpus = 1
		end		 
	end
end

----to pre download the boxes --------
$ vagrant box add  centos/7
==> box: Loading metadata for box 'centos/7'
    box: URL: https://vagrantcloud.com/centos/7
This box can work with multiple providers! The providers that it
can work with are listed below. Please review the list and choose
the provider you will be working with.
1) hyperv
2) libvirt
3) virtualbox
4) vmware_desktop

$ vagrant box add ubuntu/xenial64 
---------------------------------
$vagrant up puppetmaster
$vagrant up puppet-agent-centos
$vagrant up puppet-agent-ubuntu 

$ vagrant status
Current machine states:
puppetmaster              running (virtualbox)
puppet-agent-centos       running (virtualbox)
puppet-agent-ubuntu       running (virtualbox)

vagrant ssh puppetmaster 
vagrant ssh puppet-agent-centos
vagrant ssh puppet-agent-ubuntu

================install  atom  Editor ================
install atom.io editor  and  language-puppet  package
??install software from atom.io, then on git command line
$ apm install language-puppet
Installing language-puppet to C:\Users\Admin\.atom\packages done

====== this not need for nomral  usage ===========
# to enable to login with ip address   user/pass = vagrant/vagrant
ip addr show
vi /etc/ssh/sshd_config
PasswordAuthentication yes
systemctl restart sshd
=========================
\puppet eco-system
client-server architecture
==puppet master 
	puppet server is JVM application that provide puppet master services.
	it can be configured on centos/ubuntu with puppet server package installed.
puppet DB : opensource database 
puppet agent: deamons run on the client 
factor :

/opt/puppetlabs/puppet/bin
/opt/puppetlabs/bin

============================
for centOS  at  http://yum.puppetlabs.com/
 get the link of 	puppetlabs-release-pc1-el-7.noarch.rpm
==>then install on puppet master and  agent
    [root@puppetmaster ~]# rpm -ivh http://yum.puppetlabs.com/puppetlabs-release-pc1-el-7.noarch.rpm
==>on puppet master 
    [root@puppetmaster ~]# yum -y install puppetserver
	# rpm -q puppetserver
	puppetserver-2.8.1-1.el7.noarch

==>on centos agent
	[root@centos-agent ~]# yum -y install puppet-agent	
	# rpm -q puppet-agent
	puppet-agent-1.10.12-1.el7.x86_64

====> for ubuntu 
	http://apt.puppetlabs.com/ get address of uppetlabs-release-pc1-xenial.deb
	#  wget http://apt.puppetlabs.com/puppetlabs-release-pc1-xenial.deb
	root@ubuntu-agent:~# dpkg -i puppetlabs-release-pc1-xenial.deb
	#  apt-get -y update 
	#  apt-get -y install  puppet-agent
	
 vi /etc/profile.d/puppet-agent.sh   (on puppet master & agent)
if ! echo $PATH | grep -q /opt/puppetlabs/bin ; then
  export PATH=$PATH:/opt/puppetlabs/bin
  export PATH=$PATH:/opt/puppetlabs/puppet/bin
fi

  
 logout 
 sudo su - 
 puppet --version    (on puppet server)
 puppet agent --version   (on puppet client)
 
---------------------------------------------- 
====>On puppet master 
/etc/puppetlabs     => main configuration directoy of puppet 
/etc/puppetlabs/code/environments/production =>default environment, agents get catalog from production environment by default
/etc/puppetlabs/puppet =>contains global config files for puppet and hiera
	auth.conf  hiera.yaml  puppet.conf  ssl
/etc/puppetlabs/puppetserver => contains config files to puppet server service 

/opt/puppetlabs  => data files and binaray files related to puppet are here

cat /etc/sysconfig/puppet
# You may specify parameters to the puppet client here
#PUPPET_EXTRA_OPTS=--waitforcert=500

cat /etc/sysconfig/puppetserver
###########################################
# Init settings for puppetserver
###########################################
................

# Modify this if you'd like to change the memory allocation, enable JMX, etc
JAVA_ARGS="-Xms2g -Xmx2g -XX:MaxPermSize=256m"
# These normally shouldn't need to be edited if using OS packages
USER="puppet"
GROUP="puppet"
INSTALL_DIR="/opt/puppetlabs/server/apps/puppetserver"
CONFIG="/etc/puppetlabs/puppetserver/conf.d"

-----------------------------------------------
====> on puppetmaster
systemctl start puppetserver
netstat -ntlp    (find the java process )
vi  /etc/hosts
192.168.2.162  centos-agent.home
192.168.2.163  ubuntu-agent.home

==@on centos-agent & ubuntu-agent 
vi /etc/hosts    ; add below line
192.168.2.161    puppetmaster.home

====> on puppetmaster
cd /etc/puppetlabs/code/environments/production
cd manifests
vi site.pp
node /agent/ {
	include helloworld 
	include webserver
}
full path is /etc/puppetlabs/code/environments/production/manifests/site.pp

cd /etc/puppetlabs/code/environments/production/modules
mkdir -p helloworld/manifests
vi helloworld/manifests/init.pp
class helloworld {
  file { '/tmp/helloworld.txt':
    ensure => file,
    mode => '0644',
    content => "this hellow from puppet \n"
  }
}
full path is /etc/puppetlabs/code/environments/production/modules/helloworld/manifests/init.pp	

cd /etc/puppetlabs/code/environments/production/modules
mkdir -p webserver/manifests
vi  webserver/manifests/init.pp
class webserver {
	if $::osfamily == 'RedHat' {
		package { 'httpd' :
				ensure => present
		}
    } elsif $::osfamily == 'Debian' {
		package { 'apache2' :
				ensure => present
		}
	} else {
	}
}
full path is /etc/puppetlabs/code/environments/production/modules/webserver/manifests/init.pp	

==>on centos-agent  & ubuntu-agent
#facter 
#facter os.family
puppet agent --test --server puppetmaster.home
====Note :-
>>> if getting error like below 
Error: Could not request certificate: Connection refused - connect(2) for "puppetmaster.home" port 8140

verify puppetserver is running 
ps -ef |grep  puppet
netstat -anp |grep 8140
    ==if not running start or restart puppetserver
	systemctl start puppetserver
can try below commands too 
  =Following command is for starting the server :
puppet resource service puppetserver ensure=running
  =This command is to enable the server.
 puppet resource service puppetserver enable=true		
====Note end ===================


==>@on puppetmster 
puppet cert list 
"centos-agent.home" (SHA256) E3:04:68:12:55:F1:BF:4E:AE:52:E1:CD:02:1B:23:E7:24:21:FA:EF:12:1F:0B:
puppet cert sign centos-agent.home
puppet cert sign ubuntu-agent.home
puppet cert list --all
puppet cert clean <hostname>   ---> to clean a cert
==>@centos-agent 
puppet agent --test --server puppetmaster.home  --noop
puppet agent --test --server puppetmaster.home

==>@ubuntu-agent 
puppet agent --test --server puppetmaster.home  --noop
puppet agent --test --server puppetmaster.home

==>on puppetmaster
ls /opt/puppetlabs/server/data/puppetserver/reports/
ls -l /opt/puppetlabs/server/data/puppetserver/reports/centos-agent.home    
---this directory has the client's puppet run  reports

\===overview of puppet lang===================

---Directory strure of modules
*$modulepath/<module name>/manifests
 manifests directory contain puppet program files with .pp extension
*$modulepath/<module name>/files:
  contains files to be created on agents using 'file' resource type  with static contents
*$modulepath/<module name>/templates
  contains files to be created on agents using 'file' resource type  with dynamic contents
 
init.pp  -->first file in manifests is init.pp , the format is 
class webserver{
	<resource-type>{ <uniqe-name>:
		<attribute> => <value>
	}
}
------------------------------------
#===puppet code to install apache
vi /etc/puppetlabs/code/environments/production/manifests/site.pp
node /agent/ {
	include helloworld 
	include webserver
}

cd /etc/puppetlabs/code/environments/production/modules/
mkdir -p webserver/files
mkdir -p  webserver/templates

$modulepath/webserver/templates/vhost.conf.erb   #--> template file configure with .erb  extension
vi /etc/puppetlabs/code/environments/production/modules/webserver/templates/vhost.conf.erb
<virtualhost *:80>
    servername  <%= @fqdn %>
    DocumentRoot  /var/www/html
</virtualhost>

#vi /etc/puppetlabs/code/environments/production/modules/webserver/files/httpd.conf
# add apache config file for cent os

 cd /etc/puppetlabs/code/environments/production/modules/webserver/manifests
 vi parameters.pp
class webserver::parameters {
  if $::osfamily == 'RedHat' {
    $packagename = 'httpd'
    $configfile  = '/etc/httpd/conf/httpd.conf'
#    $configsource = 'puppet:///modules/webserver/httpd.conf'
    $vhostfile    ='/etc/httpd/conf.d/vhost.conf'
  } elsif $::osfamily == 'Debian' {
    $packagename  = 'apache2'
    $configfile   = '/etc/apache2/apache2.conf'
#    $configsource = 'puppet:///modules/webserver/apache2.conf'
    $vhostfile    = '/etc/apache2/sites-enabled/vhost.conf'
  }
}

# cd /etc/puppetlabs/code/environments/production/modules/webserver/manifests
# vi init.pp
class webserver(
        $packagename = $::webserver::parameters::packagename,
        $configfile  = $::webserver::parameters::configfile,
#        $configsource = $::webserver::parameters::configsource,
        $vhostfile    = $::webserver::parameters::vhostfile,
      ) inherits ::webserver::parameters {
    package { 'webserver-package':
      name => $packagename,
      ensure => present
    }
#    file { 'config-file':
#      path => $configfile,
#      ensure => file,
#      source => $configsource,
#      require => Package['webserver-package'],
#      notify => Service['webserver-service'], 
#    }
    file { 'vhost-file':
      path => $vhostfile,
      ensure => file,
      content => template('webserver/vhost.conf.erb'),
      require => Package['webserver-package'],
      notify => Service['webserver-service'],  
    }
    service { 'webserver-service':
      name => $packagename,
      ensure => running,
      enable => true,
      hasrestart => true,
      require => File['vhost-file']
    }
}

==> on centos-agent
 puppet agent --test --server puppetmaster.home  --noop
 puppet agent --test --server puppetmaster.home 
ps -ef |grep http
cat /etc/httpd/conf/httpd.conf
cat /etc/httpd/conf.d/vhost.conf
----------------------------------------------------------------------
===puppet server in production and managing certificates 

puppet cert list    --> to list certs which need the signing
puppet cert list  --all  --> list all certs on the puppet master

puppet cert sign <agent-name>
puppet cert sign --all  --> to sign all certs at same time

puppet cert clean <agent-name>  --> to delete certificates

##to regenrate  puppetmaster certificate on puppetmaster 
puppet cert clean  puppetmaster.home
puppet cert generate puppetmaster.home --dns_alt_names=puppet,puppetmaster,puppetserver,puppetserver.home 
puppet cert list --all
+ "centos-agent.home" (SHA256) C7:DB:D7:53:BC:E7:E6:55:0B:E7:25:75:F5:42:B2:42:B8:22:61:DB:89:82:08:77:F6:6B:07:48:56:24:DC:11
+ "puppetmaster.home" (SHA256) 4D:4F:25:2C:E6:(alt names: "DNS:puppet", "DNS:puppetmaster.home","DNS:puppetmaster","DNS:puppetserver.home")
==>puppet agents can communicate with puppetmaster with any of the alternate names

==>if the certificate not signed automatically ,sign manuall
puppet cert sign  puppetmaster.home --allow-dns-alt-names

*after cert generated, add to /etc/puppetlabs/puppet/puppet.conf
[main]
certname = puppetmaster.home
[master]
dns_alt_names = puppet,puppetmaster,puppetserver,puppetserver.home 
--then restart puppet
# systemctl restart puppetserver

===TO automatically sign  certificates 
vi /etc/puppetlabs/puppet/autosign.conf
*.home
*.example.com
*
----------------
===puppet community modules==================================================== 
community modules are generic modules developed&maitiained by puppet users hosted on 
puppet forge or github

*puppet forge is repository of puppet modules
	puppet forge has  release/version to help to keepup with version
* forge.puppet.come
--puppet forge module publish workflow
1- write  module
2- update metadata.json
3- build .tar.giz package of module
4- create account on puppet Forge
5- upload .tar.gz package in puppet Forge
6- publish module in puppet Forge

==creating a module
$cd <path>/modules
$ puppet module generate --skip-interview  <pforgeUserName>-<ModuleName>
$ pupept module generate --skip-interveiw   puser-testRepo
vi testRepo/metadata.json
"name": "puser-testRepo",
"version": "0.1.0",
"summary": "a test module"
"source": "path of github" 

$  cd testRepo
$  puppet module build
$  ls -l  pkg
puser-testRepo-0.1.0.tar.gz

====Managing Module dependencies & libararian puppet ======================


Librarian puppet ->its a tool to manage puppet dependencies, it can fetch module from pupept forge and github
root@puppetmaster]#  gem install librarian-puppet --no-rdoc --no-ri
[root@puppetmaster /]# cd /opt
[root@puppetmaster opt]# librarian-puppet  init
      create  Puppetfile
vi Puppetfile  (update the as below)
#!/usr/bin/env ruby
#^syntax detection

forge "https://forgeapi.puppetlabs.com"

# A module from the Puppet Forge
 mod 'puppetlabs-stdlib'

# A module from git
 mod 'puppetlabs-ntp',
   :git => 'git://github.com/puppetlabs/puppetlabs-ntp.git'

# A module from a git branch/tag
 mod 'puppetlabs-apt',
   :git => 'https://github.com/puppetlabs/puppetlabs-apt.git',
   :ref => '1.4.x'
----
[root@puppetmaster opt]# librarian-puppet install
[root@puppetmaster opt]# cd modules
[root@puppetmaster modules]# ls -l
drwxr-xr-x.  7 root root 4096 May  6 00:48 apt
drwxr-xr-x. 11 root root 4096 May  6 00:48 ntp
drwxr-xr-x.  9 root root 4096 May  6 00:48 stdlib
-------------------------------------------------
====Managing Environments with r10K ===========================================
environments path is 
/etc/puppetlabs/code/environments 
*default environment is 
/etc/puppetlabs/code/environments/production

vi  /etc/puppetlabs/puppet/r10k.yaml
sources:
  operations:
  remote: 'https://github.com/sjcode236/envAnirban2.git'
  basedir: '/etc/puppetlabs/code/environments'
  prefix: false


		
On GitHub create  repo  envAnirban2
https://github.com/sjcode236/envAnirban2.git

@puppetmaster 
cd /opt
git clone  https://github.com/sjcode236/envAnirban2.git
 cd envAnirban2/
[root@puppetmaster testrepo2]#     git config --global user.name  "lenov lap"
[root@puppetmaster testrepo2]#     git config --global user.email "sjbuy25@gmail.com"

librarian-puppet init
 vi Puppetfile    ---->edit the file as below
#!/usr/bin/env ruby
#^syntax detection

forge "https://forgeapi.puppetlabs.com"

# A module from the Puppet Forge
 mod 'puppetlabs-stdlib'

# A module from git
 mod 'puppetlabs-ntp',
   :git => 'git://github.com/puppetlabs/puppetlabs-ntp.git'

# A module from a git branch/tag
 mod 'puppetlabs-apt',
   :git => 'https://github.com/puppetlabs/puppetlabs-apt.git',
   :ref => '1.4.x'
#----------

 mkdir manifests
 vi manifests/site.pp
node /agent/ {
        include testrepo2
}

vi environments.conf 
modulepath = site:modules:$basemodulepath
manifest = manifests/site.pp
# ls
environments.conf  manifests  Puppetfile

next create testrepo2  at github.com
https://github.com/sjcode236/testrepo2.git

@puppetmaster 
cd /opt
git clone https://github.com/sjcode236/testrepo2.git
[root@puppetmaster testrepo2]#     git config --global user.name  "lenov lap"
[root@puppetmaster testrepo2]#     git config --global user.email "sjbuy25@gmail.com"

 cd testrepo2/
mkdir manifests
touch manifests/init.pp
vi manifests/init.pp
class testrepo2  {
    if $environment == 'production' {
      notify { 'default-message' : 
              message => " this is the production env"
            }
    } else {
            notify { 'default-message' :
                 message => "This is not production"
            }
    }  
}

# git add -A
# git commit -m "adding testrepo2"
[root@puppetmaster testrepo2]# git push  origin master
Username for 'https://github.com': sjcode236
Password for 'https://sjcode236@github.com':

cd /opt/envAnirban2
vi Puppetfile
----> add at end of file 
 mod 'testrepo2',
   :git => 'https://github.com/sjcode236/testrepo2.git',
   :ref => 'master'
git add -A
git commit -m "adding env files"
# git push origin master
git branch production
git branch staging
git branch test
# git checkout production
Switched to branch 'production'
# git push origin production
# git checkout staging
Switched to branch 'staging'
# git push origin staging
# git checkout test
Switched to branch 'test'
# git push origin test

----->  next install r10k
cd 
[root@puppetmaster envAnirban2]# gem install r10k --no-rdoc --no-ri
Fetching: colored-1.2.gem (100%)
Successfully installed colored-1.2
Fetching: cri-2.6.1.gem (100%)
Successfully installed cri-2.6.1
Fetching: log4r-1.1.10.gem (100%)
Successfully installed log4r-1.1.10
Fetching: multi_json-1.13.1.gem (100%)
Successfully installed multi_json-1.13.1
Fetching: r10k-2.6.2.gem (100%)
Successfully installed r10k-2.6.2
5 gems installed

#  r10k  deploy environment -p -c   /etc/puppetlabs/puppet/r10k.yaml


=================================================

	




	  

	  























