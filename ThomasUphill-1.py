
==Learn Notes===================

Mastering Puppet - Second Edition
by Thomas Uphill
Packt Publishing, 2016


`===Using Librarian====

***Librarian is a bundler for Ruby. It handles dependency checking for you. The project for using Librarian with Puppet
is called librarian-puppet and is available at http://rubygems.org/gems/librarian-puppet. 
 To install librarian-puppet,we'll use RubyGems 

[root@stand ~]# puppet resource package librarian-puppet ensure=installed provider=gem
Notice: /Package[librarian-puppet]/ensure: created
package { 'librarian-puppet':
ensure => ['2.2.1'],
}

[root@stand ~]# librarian-puppet version
librarian-puppet v2.2.1

***The librarian-puppet project uses a Puppetfile to define the modules that will be installed. 
The syntax is the name of the module followed by a comma and the version to install.
Modules may be pulled in from Git repositories or directly from Puppet Forge. 
You can override the location of Puppet Forge using a forge line as well. 
 sample  Puppetfile would be the following:

forge "http://forge.puppetlabs.com"
mod 'puppetlabs/puppetdb', '5.0.0'
mod 'puppetlabs/stdlib', '4.9.0'

==> create a new public directory in /tmp/public4 and include the Puppetfile in that directory, as shown here:

[git@stand ~]$ cd /tmp
[git@stand tmp]$ mkdir public4 && cd public4
[git@stand public4]$ cat<<EOF>Puppetfile
> forge "https://forgeapi.puppetlabs.com"
>mod 'puppetlabs/puppetdb', '5.0.0'
>mod 'puppetlabs/stdlib', '4.9.0'
> EOF
==>Next, we'll tell librarian-puppet to install everything we've listed in the Puppetfile as follows:

[git@stand public4]$ librarian-puppet update
[git@stand public4]$ ls
modules  Puppetfile  Puppetfile.lock
***The Puppetfile.lock file is a file used by librarian-puppet to keep track of installed versions and dependencies;


`==== Using r10k  ********************************************************************************************
r10k is an automation tool for Puppet environments. It is hosted on GitHub at 
https://github.com/puppetlabs/r10k. 
 
***r10k is like  librarian-puppet and Git hooks in a single package.
 r10k takes the Git repositories specified in /etc/puppetlabs/r10k/r10k.yaml and checks out each branch of the repositories into a subdirectory of the environment directory (the environment directory is also specified in /etc/puppetlabs/r10k/r10k.yaml). 
 If there is a Puppetfile in the root of the branch, then r10k parses the file in the same way that librarian-puppet does and it installs the specified modules in a directory named modules under the environment directory.
 
*** install the r10k gem :
# puppet resource package r10k ensure=present provider=gem
Notice: /Package[r10k]/ensure: created
package { 'r10k':
ensure => ['2.0.3'],
}
=>Next, we'll create a /etc/puppetlabs/r10k/r10k.yaml file to point to our local Git repository.
 We will also specify that our Puppet environments will reside in /etc/puppetlabs/code/environments, as shown in the following snippet:

---
cachedir: '/var/cache/r10k'
sources:
control:
remote: '/var/lib/git/control.git'
basedir: '/etc/puppetlabs/code/environments'
Now, we need to create the cache directory and make it owned by the puppet user. We will use the following commands to do so:

# mkdir /var/cache/r10k
# chown puppet:puppet /var/cache/r10k
==>Now, we need to check out our code and add a Puppetfile to the root of the checkout. In each environment, create a Puppetfile that contains which modules you want installed in that environment; we'll copy the previous Puppetfile as shown in the following code:

forge "http://forge.puppetlabs.com"
mod 'puppetlabs/puppetdb', '5.0.0'
mod 'puppetlabs/stdlib', '4.9.0'

=>We'll check the syntax of our Puppetfile using r10k as shown here:

[ control]$ cat Puppetfile 
forge "http://forge.puppetlabs.com"
mod 'puppetlabs/puppetdb', '5.0.0'
mod 'puppetlabs/stdlib', '4.9.0'
[control]$ r10k puppetfile check
Syntax OK

Now, add the Puppetfile to the Git repository using the following commands:

[samdev@stand control]$ git add Puppetfile
[samdev@stand control]$ git commit -m "adding Puppetfile"

Now, r10k expects that the modules specified in the Puppetfile will get installed in $environment/modules,

ow we can test r10k using r10k deploy as follows:

[puppet@stand code]$ r10k deploy environment -p
[puppet@stand code]$ ls environments
master  production  puppet_sync  quiet  thomas
 
 
 
 
 
 
 



