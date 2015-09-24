#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink
import sys

def emptyNet():

    ## Taking hosts and number of switches as arguments.
    ## Total number of hosts = hosts * switches

    hosts = int(sys.argv[1])
    numSch = int( sys.argv[2])
    
    ## Making mininet object. TCLink is used in which bandwidth parameter is 
    ## used to specify bandwidth respectively for even and odd hosts

    net = Mininet( controller=Controller ,  link=TCLink)

    info( '*** Adding controller\n' )
    net.addController( 'c0' )
    
    info( '*** Adding hosts\n' )
    
    switches = []
    cnt=1    

    # Defining subnet networks
    ip1='10.0.1.'
    ip2='10.0.2.'

    for i in range(numSch):
        s = net.addSwitch('s'+str(i+1))  ## Adding Switches
        for j in range(hosts):            
            ind=cnt
            cnt= cnt+1
            if ind % 2 !=0:
                h = net.addHost( 'h'+str(cnt), ip=ip1+str(ind)+'/24')   ## Adding Odd host to 10.0.1.0 subnet
                net.addLink( h, s, bw=1 )                               ## Adding links between switch and hosts
            else:
                h = net.addHost( 'h'+str(cnt), ip=ip2+str(ind)+'/24')   ## Adding Even host to 10.0.2.0 subnet
                net.addLink( h, s , bw=2 )
        switches.append(s)

    for i in range(numSch):
        if i < numSch-1:
            net.addLink(switches[i], switches[i+1], bw=2)   ## Adding links between switches

    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
