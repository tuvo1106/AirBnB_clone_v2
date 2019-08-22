# Prepare web servers

exec { 'update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update']
}

file { ['/data/', '/data/web_static/', '/data/web_static/releases/', '/data/web_static/releases/test', '/data/web_static/shared']:
   ensure => 'directory',
    owner => 'ubuntu',
    group => 'ubuntu',
}

file { '/data/web_static/releases/test/index.html':
   content => "<html>
   <head>
   </head>
   <body>
     Holberton School
   </body>
   </html>",
     owner => 'ubuntu',
     group => 'ubuntu',
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test/',
  force  => yes,
   owner => 'ubuntu',
   group => 'ubuntu',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
