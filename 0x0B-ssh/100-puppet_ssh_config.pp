#!/usr/bin/env bash
#client SSH configuration using Puppet

file {'etc/ssh/ssh_config':
	ensure  => present,
	content => "
		host*
		IdentityFile ~/.ssh/school
		passwordAuthentication no
		",
}
