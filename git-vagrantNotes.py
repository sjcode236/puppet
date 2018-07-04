

====================================================
Notepad++  and atom.io  editors 

`====putty download=========
https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html

http://cmder.net/   (for ssh on windows )

https://git-scm.com/downloads
===============================================

setting up Vagrant for chef and package a vagrant box
https://gist.github.com/dergachev/3866825

Setting Up Vagrant Environment on Windows Platform
https://github.com/saasbook/courseware/wiki/Setting-Up-Vagrant-Environment-on-Windows-Platform

===========================================================
https://www.vagrantup.com/downloads.html
   download windows 64 bit vagrant and install 

vagrant list-commands
vagrant box add ADDRESS

vagrant box list
vagrant box prune
     This command removes old versions of installed boxes. 
vagrant box remove NAME
--all - Remove all available versions of a box.
--force - Forces removing the box even if an active Vagrant environment is using it.
--provider VALUE - The provider-specific box to remove with the given name. 	 
vagrant box update
--box VALUE - Name of a specific box to update. If this flag is not specified, Vagrant will update the boxes for the active Vagrant environment.
--provider VALUE - When --box is present, this controls what provider-specific box to update. 

vagrant up
vagrant halt
vagrant destroy
vagrant status

---download  vagrant images from vagrantcloud.com
------ to download  OS iamges/box  to vargrant
 vagrant box add precise64 http://files.vagrantup.com/precise64.box # 323MB, faster download
 vagrant box add "centos/7"
 vagrant box add "ubuntu/xenial64"

vagrant up puppetmaster
vagrant halt puppetmaster 

----vagrant file for multiple vms ----------
Vagrant.configure("2") do |config|
    config.vm.provider "virtualbox" do |v|
		v.memory = 1800
		v.cpus = 1
	end
# make sure vm ips  different from LAN ips of other devicesa
	config.vm.define "puppetmaster" do |pm|
		pm.vm.box = "centos/7"
		pm.vm.network "private_network",ip: "192.168.2.161"
		pm.vm.hostname = "puppetmaster"
	end
	config.vm.define "puppet-agent-centos" do |pac|
		 pac.vm.box = "centos/7"
		 pac.vm.network "private_network",ip: "192.168.2.162"
		 pac.vm.hostname = "centos-agent"
	end
	config.vm.define "puppet-agent-ubuntu" do |pau|
		 pau.vm.box = "ubuntu/xenial64"
		 pau.vm.network "private_network",ip: "192.168.2.163"
		 pau.vm.hostname = "ubuntu-agent"
	end
end
--------------------------------------------------------------
#to make vms with different cpus & memory

Vagrant.configure("2") do |config|
# make sure vm ips  different from LAN ips of other devicesa
        config.vm.define "puppetmaster" do |pm|
                pm.vm.box = "centos/7"
                pm.vm.network "private_network",ip: "192.168.2.161"
                pm.vm.hostname = "puppetmaster"
                pm.vm.provider "virtualbox" do |vpm|
                        vpm.memory = 2048
                        vpm.cpus = 2
                end
        end
        config.vm.define "puppet-agent-centos" do |pac|
                pac.vm.box = "centos/7"
                pac.vm.network "private_network",ip: "192.168.2.162"
                pac.vm.hostname = "centos-agent"
                pac.vm.provider "virtualbox" do |vpac|
                        vpac.memory = 1800
                        vpac.cpus = 1
                end
        end
        config.vm.define "puppet-agent-ubuntu" do |pau|
                pau.vm.box = "ubuntu/xenial64"
                pau.vm.network "private_network",ip: "192.168.2.163"
                pau.vm.hostname = "ubuntu-agent"
                pau.vm.provider "virtualbox" do |vpau|
                        vpau.memory = 1750
                        vpau.cpus = 1
                end
        end
end

--------------------------------------------------

====git installation section=========
====putty download=========
https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html

http://cmder.net/   (for ssh on windows )

https://git-scm.com/downloads
===download and install Git-2.17.0-64-bit
during installation select 
"Use Git and optional Unix tools from the windows Command prompt"
then launch git bash  
start->git->git bash

-create a folder -> right click on it -> Git bash here
   touch index.html
   touch app.py
    git init
    git config --global user.name  "lenov lap"
    git config --global user.email "sjbuy25@gmail.com"
    git add  
    git index.html
    git *.html
    git status
    git rm --cached index.html
    git status
    git add .
vi index.html  (add  some text)
git commit -m 'changed  index.html'

git branch login
$ git checkout login
Switched to branch 'login'
git status
touch login.html ( add some text)
git add .
git status
git commit -m 'login form'
git checkout master
git branch   -->  to see  what branch on now 
git merge login -m 'merging the login branch'
=====git with github===
on github.com create a repo 'Gitapp1'
echo "# Gitapp1" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/sjcode236/Gitapp1.git
git push -u origin master

mkdir dir1
mkdir dir2
git commit -m "adding dir1 dir2"
git push
Now all the files will be on github.come
make a change to index.html  on github then
git pull -> will update all local file

to clone 
git clone https://github.com/sjcode236/Gitapp1.git
---------------------------------------
===install git on centos linux =====
yum install git
git --version
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --list
	user.name=Your Name
	user.email=you@example.com

# Set the cache to timeout after 1 hour (setting is in seconds)
git config --global credential.helper 'cache --timeout=3600'
git push origin master 


====================================
***TO see all branches
git branch --all

***TO see on which branch  now checkout to
[root@puppetmaster envAnirban2]# git branch
  master
  production
  staging
* test

***To delete  remote branch at  github  
git push origin --delete  staging    
 
***Deleting a local branch:
git branch --delete <branch>
git branch -d <branch> # Shorter version
git branch -D <branch> # Force delete un-merged branches
***Deleting a local remote-tracking branch:
git branch --delete --remotes <remote>/<branch>
git branch -rd <remote>/<branch> # Shorter
git branch -rd  origin/staging

git fetch <remote> --prune # Delete multiple obsolete tracking branches
git fetch <remote> -p      # Shorter
***Note that this removes all obsolete local remote-tracking branches for any remote branches that no longer exist on the remote:

 

