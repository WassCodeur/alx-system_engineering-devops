# increase user limit

exec{'harrd-limit':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits/conf',
  path    => '/usr/bin/env'
}
exec{'soft-limit':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits/conf',
  path    => '/usr/bin/env'
   }
