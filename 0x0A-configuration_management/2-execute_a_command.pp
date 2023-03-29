# Executes a bach command
exec { 'kill':
    command => 'pkill -f killmenow',
    path    => ['/usr/bin', '/usr/sbin']
}
