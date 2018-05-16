
==Learn Notes===================

Mastering Puppet - Second Edition
by Thomas Uphill
Packt Publishing, 2016


`===Using Librarian====

***Librarian is a bundler for Ruby. It handles dependency checking for you. The project for using Librarian with Puppet is called librarian-puppet and is available at http://rubygems.org/gems/librarian-puppet. To install librarian-puppet, we'll use RubyGems 

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

