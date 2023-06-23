# increase user limit

exec{'hard-limit':
  command => 'sed -i "s/4/20000/; s/5/20000" /etc/security/limits.conf',
  path    => '/usr/bin/env'
}
