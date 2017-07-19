# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from os import popen2


def set_ip(interface, ip):
    print popen2(['ip','addr','add', ip, 'dev', interface])


def get_wireless_interfaces():
    '''
        Read /proc/net/wireless and return a list of interfaces
        :return: type list interfaces
    '''
    self.interfaces=[]
    self.proc_netdev = open("/proc/net/wireless", 'r').read().split('\n')
    self.proc_netdev.pop(0)
    self.proc_netdev.pop(0)
    self.proc_netdev.remove('')
    for line in self.proc_netdev:
        self.interfaces.append(line.split(' ').pop(1).split(':').pop(0))
        return self.interfaces

