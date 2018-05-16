


Mastering Puppet - Second Edition
by Thomas Uphill
Packt Publishing, 2016


`===Using Librarian====
https://www.safaribooksonline.com/library/view/mastering-puppet-/9781785888106/ch04s04.html#
***Librarian is a bundler for Ruby. It handles dependency checking for you. The project for using Librarian with Puppet is called librarian-puppet and is available at http://rubygems.org/gems/librarian-puppet. To install librarian-puppet, we'll use RubyGems 

[root@stand ~]# puppet resource package librarian-puppet ensure=installed provider=gem
Notice: /Package[librarian-puppet]/ensure: created
package { 'librarian-puppet':
ensure => ['2.2.1'],
}

