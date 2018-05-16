
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



