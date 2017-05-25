######################
#Author: Alex Leung ##
######################

from API.Utility import UtilConst
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Device.Switch.Switch import Switch



#function initialization
util = Util()
sw0 = Switch(ComponentBoxConst.DeviceModel.SWITCH_IE_2000, 100, 100, "Switch0")


def main():
    util.init()
    maketop()
    functions()

def maketop():
    sw0.create()
    util.speedUpConvergence()
    sw0.select()
    sw0.clickCliTab()
    sw0.cli.startConsole()
    sw0.cli.setCliText('''
en
conf t
license boot level enhancedlanbase
yes
end

copy run start

reload
''')
    sw0.close()
    util.speedUpConvergence()
    snooze(1)
    
def functions():
    sw0.select()
    sw0.clickCliTab()
    sw0.cli.startConsole()
    sw0.cli.setCliText('''
en
conf t
int gig1/1
l2nat test''')
    sw0.cli.textCheckPoint("Couldn't find the Instance test", 1)
    sw0.cli.setCliText('''l2nat instance test''')
    sw0.cli.textCheckPoint("Couldn't find the Instance instance", 1)
    sw0.cli.setCliText('''exit
l2nat instance test
int g1/1
l2nat test1 1''')
    sw0.cli.textCheckPoint("Couldn't find the Instance test1", 1)
    sw0.cli.setCliText('''exit
l2nat instance test
outside from host 1.1.1.1 to 2.2.2.2
int gig1/1
l2nat test''')
    sw0.cli.textCheckPoint("Warning: This will translate untagged vlan traffic. To translate tagged vlan traffic enter vlan id.", 1)
    sw0.cli.setCliText('''l2nat test testing1''')
    sw0.cli.textCheckPoint("Error: Invalid vlan range specification: Character #1 't' is non-numeric", 1)
    sw0.cli.setCliText('''l2nat test 99999999''')
    sw0.cli.textCheckPoint("Error\: Invalid vlan range specification\: Character \#9 delimits a number which is out of the range \(1...4094\)", 1)
    sw0.cli.setCliText('''l2nat test 0''')
    sw0.cli.textCheckPoint("Error\: Invalid vlan range specification\: Character \#2 delimits a number which is out of the range \(1...4094\)", 1)
    sw0.cli.setCliText('''l2nat test 18-20
l2nat test 18''')
    sw0.cli.textCheckPoint("Instance already attached to this interface-vlan", 1)
    sw0.cli.setCliText('''l2nat test 21-22
l2nat test 40-2095''')
    sw0.cli.textCheckPoint("Max Instance limit of 128 reached", 1)
    sw0.cli.setCliText('''l2nat test 4094-095''')
    sw0.cli.textCheckPoint("Error\: Invalid vlan range specification\: Character \#9 delimits a number\(95\) of the range, which is not greater than the starting number\(4094\)", 1)
    sw0.cli.setCliText('''exit
l2nat instance test
outside from network 1.1.1.1 to 2.2.2.2 mask 0.0.0.0''')
    sw0.cli.textCheckPoint("Error. Invalid subnet_mask 0.0.0.0", 1)
    sw0.cli.setCliText('''outside from network 1.1.1.1 to 2.2.2.2 mask 1.1.1.1''')
    sw0.cli.textCheckPoint("Error. Invalid subnet_mask 1.1.1.1", 1)
    sw0.cli.setCliText('''outside from network 1.1.1.1 to 2.2.2.2 mask 255.255.255.255''')
    sw0.cli.textCheckPoint("Error. Invalid subnet_mask 255.255.255.255", 1)
    sw0.cli.setCliText('''outside from network 1.1.1.1 to 2.2.2.2 mask 255.255.255.0
outside from range 1.1.1.1 to 2.2.2.2 55''')
    sw0.cli.textCheckPoint("Error. Overlaps with network address already configured", 1)
    sw0.cli.setCliText('''outside from range 2.2.2.2 to 2.2.2.2 128''')
    sw0.cli.textCheckPoint("Error. Original ip and Translated ip is the same.", 1)
    sw0.cli.setCliText('''outside from range 2.2.2.2 to 2.2.2.3 128''')
    sw0.cli.textCheckPoint("Max Translations limit of 128 exceeded", 1)
    sw0.cli.setCliText('''outside from host 1.1.1.1 to 2.2.2.2''')
    sw0.cli.textCheckPoint("Error. Overlaps with network address already configured", 2)
    sw0.cli.setCliText('''inside from host 4.4.4.4 to 3.3.3.3
no outside from range 2.2.2.2 to 3.3.3.3 22''')
    sw0.cli.textCheckPoint("Error. No matching translation found", 1)
    sw0.cli.setCliText('''no outside from network 1.1.1.1 to 2.2.2.2 mask 255.255.255.0''')
    sw0.cli.textCheckPoint("Error: Couldn't find this translation in the instance test", 1)
    sw0.cli.setCliText('''no outside from network 1.1.1.0 to 2.2.2.0 mask 255.255.255.0''')
    sw0.cli.textCheckPoint("Switch\(config-l2nat\)\#no outside from network 1.1.1.0 to 2.2.2.0 mask 255.255.255.0\nSwitch\(config-l2nat\)\#", 1)
    sw0.cli.setCliText('''outside from range 4.4.4.4 to 4.4.4.6 2
outside from range 4.4.4.5 to 4.4.4.6 2''')
    sw0.cli.textCheckPoint("Error. Translated ip overlaps with translated ip of the range translation already configured", 1)
    sw0.cli.setCliText('''outside from range 4.4.4.7 to 4.4.4.6 2''')
    sw0.cli.textCheckPoint("Error. Translated ip overlaps with translated ip of the range translation already configured", 2)
    sw0.cli.setCliText('''outside from range 4.4.4.6 to 4.4.4.8 2''')
    sw0.cli.textCheckPoint("Error. The original address overlaps with the translated address already configured.", 1)
    sw0.cli.setCliText('''no outside from network 1.1.1.0 to 2.2.2.0 mask 255.255.255.0
exit
int g1/1
no l2nat test''')
    sw0.cli.setCliText('''no l2nat test 55''')
    sw0.cli.textCheckPoint("Error: No entry found for interface GigabitEthernet1/1 with instance name test and vlan 55", 1)
    sw0.cli.setCliText('''no l2nat test 1
no l2nat test 10-21
no l2nat test 18-21
''')
    sw0.cli.textCheckPoint("Error\: No entry found for interface GigabitEthernet1/1 with instance name test and vlan 18\nError\: No entry found for interface GigabitEthernet1/1 with instance name test and vlan 19\nError\: No entry found for interface GigabitEthernet1/1 with instance name test and vlan 20\nError\: No entry found for interface GigabitEthernet1/1 with instance name test and vlan 21", 1)
    sw0.cli.setCliText('''do show run
      ''')
    sw0.cli.textCheckPoint("l2nat instance test\n instance-id 1\n fixup arp\n fixup icmp\n inside from host 4.4.4.4 to 3.3.3.3\n outside from range 4.4.4.4 to 4.4.4.6 2", 1)
    sw0.cli.setCliText('''do show l2nat stat
         ''')
    sw0.cli.textCheckPoint("TRANSLATED STATS \(IN PACKETS\)", 1)
    sw0.cli.textCheckPoint("Gi1\/1     EGRESS    22     0           0           0           0", 2)
    sw0.cli.textCheckPoint("Gi1\/1     INGRESS   22     0           0           0           0", 2)
    #one for the translated stats table, one for the igmp/multicast table
    sw0.cli.textCheckPoint("PROTOCOL FIXUP STATS \(IN PACKETS\)", 1)
    sw0.cli.textCheckPoint("Gi1\/1     EGRESS    22     0           0", 3)
    sw0.cli.textCheckPoint("Gi1\/1     INGRESS   22     0           0", 3)
    sw0.cli.textCheckPoint("IGMP AND MULTICAST STATS \(IN PACKETS\)", 1)
    sw0.cli.textCheckPoint("PER TRANSLATION STATS \(IN PACKETS\)", 1)
    sw0.cli.textCheckPoint("OUTSIDE  INGRESS    SA    4.4.4.4        4.4.4.6         0         0", 1)
    sw0.cli.textCheckPoint("OUTSIDE  EGRESS     DA    4.4.4.6        4.4.4.4         0         0", 1)
    sw0.cli.textCheckPoint("OUTSIDE  INGRESS    SA    4.4.4.5        4.4.4.7         0         0", 1)
    sw0.cli.textCheckPoint("OUTSIDE  EGRESS     DA    4.4.4.7        4.4.4.5         0         0", 1)
    sw0.cli.textCheckPoint("NUMBER OF ACTIVE TRANSLATIONS IN THE PAST 90 SECONDS: 0", 1)
    sw0.cli.textCheckPoint("TOTAL TRANSLATIONS : 3", 1)
    sw0.cli.textCheckPoint("TOTAL INSTANCES ATTACHED: 1", 1)
    sw0.cli.textCheckPoint("Total Number of NAT Packets               = 0", 1)
    sw0.cli.textCheckPoint("Total Number of TRANSLATED NAT  Packets   = 0", 1)
    sw0.cli.textCheckPoint("Total Number of BYPASSED   NAT  Packets   = 0", 1)
    sw0.cli.textCheckPoint("Total Number of DISCARDED  NAT  Packets   = 0", 1)
    sw0.cli.textCheckPoint("Total Number of ARP      FIX UP Packets   = 0", 1)
    sw0.cli.textCheckPoint("Total Number of ICMP     FIX UP Packets   = 0", 1)
    sw0.cli.textCheckPoint("Total Number of IPV4 MULTICAST  Packets   = 0", 1)
    sw0.cli.textCheckPoint("Total Number of IGMP            Packets   = 0", 1)
    sw0.cli.textCheckPoint("Total Number of UNMATCHED       Packets   = 0", 1)
    sw0.cli.textCheckPoint("Total Number of IPV4 UNICAST    Packets   = 0", 1)
    sw0.cli.setCliText('''end

show l2nat stat int gi1/1

show l2nat instance
      ''')
    sw0.cli.textCheckPoint("l2nat instance test\n fixup  : arp, icmp\n  inside from host 4.4.4.4 to 3.3.3.3\n  outside from range 4.4.4.4 to 4.4.4.6 2", 1)
    #sw0.cli.setCliText('''show l2nat instance nonExisting
    #  ''')
    #sw0.cli.textCheckPoint("Switch\#show l2nat instance nonExisting\nSwitch\#", 1)
    #PT only suports "show l2nat instance" command
    sw0.cli.setCliText('''show l2nat stat instance test
      ''')
    #2 from the previous "show l2nat stat" command, one for the translated stats table, one for the igmp/multicast table
    sw0.cli.textCheckPoint("Gi1\/1     EGRESS    22     0           0           0           0", 6)
    sw0.cli.textCheckPoint("Gi1\/1     INGRESS   22     0           0           0           0", 6)
    sw0.cli.textCheckPoint("OUTSIDE  INGRESS    SA    4.4.4.4        4.4.4.6         0         0", 2)
    sw0.cli.textCheckPoint("OUTSIDE  EGRESS     DA    4.4.4.6        4.4.4.4         0         0", 2)
    sw0.cli.textCheckPoint("OUTSIDE  INGRESS    SA    4.4.4.5        4.4.4.7         0         0", 2)
    sw0.cli.textCheckPoint("OUTSIDE  EGRESS     DA    4.4.4.7        4.4.4.5         0         0", 2)
    sw0.cli.cliText
    sw0.close()
