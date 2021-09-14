from mtv.net import Virtualnet
from mtv.cli import CLI
from mtv.rest import REST
from mtv.log import info
import random

net = Virtualnet(docker=True, metrics=True)

# Add Controller
info('*** Adding controller\n')
net.addController('c0')

# Add Central Switch
info('*** Adding switches\n')
swid = str(random.randint(1, 999))
s1 = net.addSwitch('s' + swid)

# Intermediary Switches to connect nodes.
sh1 = net.addSwitch('sa'+swid)
sh2 = net.addSwitch('sb'+swid)
sh3 = net.addSwitch('sc'+swid)
sh4 = net.addSwitch('sd'+swid)

# Add Namespaces and Links
info('*** Adding Hosts\n')
h1 = net.addHost('h1')
h2 = net.addHost('h2')
h3 = net.addHost('h3')
h4 = net.addHost('h4')
h5 = net.addHost('h5')
h6 = net.addHost('h6')
h7 = net.addHost('h7')
h8 = net.addHost('h8')
net.addLink(h1, sh1)
net.addLink(h2, sh1)
net.addLink(h3, sh2)
net.addLink(h4, sh2)
net.addLink(h5, sh3)
net.addLink(h6, sh3)
net.addLink(h7, sh4)
net.addLink(h8, sh4)

# Add Click Vms Plus Links to switches
info('*** Adding VMs\n')
click1_defaults = {'switches': ['s'+swid, 'sa'+swid, 'sb'+swid]}
click2_defaults = {'switches': ['s'+swid, 'sc'+swid, 'sd'+swid]}
click1 = net.addVNode('c1', '/mnt/libvirt.xml', **click1_defaults)
click2 = net.addVNode('c2', '/mnt/libvirt.xml', **click2_defaults)

info('*** Starting network\n')
net.start()
info('*** Running CLI\n')
REST(net)
CLI(net)
info('*** Stopping network')
net.stop()
