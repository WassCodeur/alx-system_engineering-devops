# Sky is the limit, let's bring that limit higher
exec{'IncreaseLimit':
  command => 'sed -i "s/15/1000/" /etc/default/nginx',
  path    => '/usr/bin/env'
}
exec{'restartNginx':
  command => 'service nginx restart',
  path    => '/usr/bin/env'
}
