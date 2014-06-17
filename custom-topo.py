from mininet.topo import Topo
 
class CustomTopo(Topo):
"Simple Data Center Topology"
 
"linkopts - (1:core, 2:aggregation, 3: edge) parameters"
"fanout - number of child switch per parent switch"
def __init__(self, linkopts1, linkopts2, linkopts3, fanout=2, **opts):
# Initialize topology and default options
Topo.__init__(self, **opts)
# Numbering: h1..N, s1..M
self.hostNum = 1
self.switchNum = 1
self.addTree([linkopts1, linkopts2, linkopts3], fanout);
 
# Derived from class TreeTopo
def addTree(self, linkopts, fanout, depth=0):
isSwitch = depth < 3
if isSwitch:
node = self.addSwitch('s%s' % self.switchNum)
self.switchNum += 1
for _ in range(fanout):
child = self.addTree(linkopts, fanout, depth + 1)
self.addLink(node, child, **linkopts[depth])
else:
# host
node = self.addHost('h%s' % self.hostNum)
self.hostNum += 1
return node
 
topos = { 'custom': ( lambda: CustomTopo() ) }
 
from mininet.log import setLogLevel
setLogLevel('info')
