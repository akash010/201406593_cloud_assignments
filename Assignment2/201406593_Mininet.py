#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink
import sys

def emptyNet():

    hosts = int(sys.argv[1])
    numSch = int( sys.argv[2])
    
    net = Mininet( controller=Controller ,  link=TCLink)

    info( '*** Adding controller\n' )
    net.addController( 'c0' )
    
    info( '*** Adding hosts\n' )
    
    switches = []
    cnt=1    

    ip1='10.0.1.'
    ip2='10.0.2.'

    for i in range(numSch):
    s = net.addSwitch('s'+str(i+1)) 
        for j in range(hosts):            
        ind=cnt
        cnt= cnt+1
        if ind % 2 !=0:
                h = net.addHost( 'h'+str(cnt), ip=ip1+str(ind)+'/24')
                net.addLink( h, s, bw=1 )
        else:
                h = net.addHost( 'h'+str(cnt), ip=ip2+str(ind)+'/24')
                net.addLink( h, s , bw=2 )
        switches.append(s)

    for i in range(numSch):
    if i < numSch-1:
            net.addLink(switches[i], switches[i+1], bw=2)

    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
