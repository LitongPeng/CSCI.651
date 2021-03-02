from packet import Packet
import datetime


# Process the first 34 bytes of the ipv4 packet
def parse_ipv4(line):
    print(line)
    print("Destination Hardware Address:" + line[:18].replace('|', ' ') + ', '
          + "Source Hardware Address:" + line[18:36].replace('|', ' ') + ', '
          + "Type:" + line[36:42].replace('|', ' ') + ', '
          + "Version:" + line[42:44].replace('|', ' ') + ', '
          + "Header Length:" + line[44:46].replace('|', ' ') + ', '
          + "Differentiated Services Fields:" + line[46:49].replace('|', ' ') + ', '
          + "Total Length:" + line[49:55].replace('|', ' ') + ', '
          + "Identification:" + line[55:61].replace('|', ' ') + ', '
          + "Flags:" + line[61:64].replace('|', ' ') + ', '
          + "Fragment Offset:" + line[64:67].replace('|', ' ') + ', '
          + "Time to Live:" + line[67:70].replace('|', ' ') + ', '
          + "Protocol:" + line[70:73].replace('|', ' ') + ', '
          + "Header Checksum:" + line[73:79].replace('|', ' ') + ', '
          + "ip Source Address:" + line[79:91].replace('|', ' ') + ', '
          + "ip Destination Address:" + line[91:103].replace('|', ' ') + ', ')


# Process the 64 bytes of the Report igmp packet
def parse_igmp16(line):
    print(line)
    parse_ipv4(line)
    print("Options:" + line[103:114].replace('|', ' ') + ', '
          + "Type:" + line[114:117].replace('|', ' ') + ', '
          + "Max Resp Time:" + line[117:120].replace('|', ' ') + ', '
          + "Checksum:" + line[120:126].replace('|', ' ') + ', '
          + "Multicast Address:" + line[126:138].replace('|', ' ') + ', ')


# Process the first 64 bytes of the end of the Qeury igmp packet
def parse_igmp11(line):
    print(line)
    parse_ipv4(line)
    print("Type:" + line[103:106].replace('|', ' ') + ', '
          + "Max Resp Time:" + line[106:109].replace('|', ' ') + ', '
          + "Checksum:" + line[109:115].replace('|', ' ') + ', '
          + "Multicast Address:" + line[115:127].replace('|', ' ') + ', '
          )


# Process the first 64 bytes of the icmp packet
def parse_icmp(line):
    parse_ipv4(line)
    print("icmp Type:" + line[10:106].replace('|', ' ') + ', '
          + "icmp Code:" + line[106:109].replace('|', ' ') + ', '
          + "Checksum:" + line[109:115].replace('|', ' ') + ', '
          + "Identifier:" + line[115:121].replace('|', ' ') + ', '
          + "Sequence Number:" + line[121:127].replace('|', ' ') + ', '
          + "Data:" + line[127:193].replace('|', ' ') + ', ')


# Process the first 64 bytes of the tcp packet
def parse_tcp(line):
    parse_ipv4(line)
    print("Source Port:" + line[103:109].replace('|', ' ') + ', '
          + "Destination Port:" + line[109:115].replace('|', ' ') + ', '
          + "Sequence Number:" + line[115:127].replace('|', ' ') + ', '
          + "Acknoledge Number:" + line[127:139].replace('|', ' ') + ', '
          + "Header Length:" + line[139:141].replace('|', ' ') + ', '
          + "Flags:" + line[141:146].replace('|', ' ') + ', '
          + "Window:" + line[146:152].replace('|', ' ') + ', '
          + "Checksum:" + line[152:158].replace('|', ' ') + ', '
          + "Urgent Pointer:" + line[158:164].replace('|', ' ') + ', ')


# Process the first 64 bytes of the udp packet
def parse_udp(line):
    parse_ipv4(line)
    print("Source Port:" + line[103:109].replace('|', ' ') + ', '
          + "Destination Port:" + line[109:115].replace('|', ' ') + ', '
          + "Length:" + line[115:121].replace('|', ' ') + ', '
          + "Checksum:" + line[121:127].replace('|', ' ') + ', '
          + "Data:" + line[127:193].replace('|', ' ') + ', ')


# Process the first 64 bytes of the arp packet
def parse_arp(line):
    print(line)
    print("Destination Hardware Address:" + line[:18].replace('|', ' ') + ', '
          + "Source Hardware Address:" + line[18:36].replace('|', ' ') + ', '
          + "Type:" + line[36:42].replace('|', ' ') + ', '
          + "Hardware type:" + line[42:48].replace('|', ' ') + ', '
          + "Protocol Type:" + line[48:54].replace('|', ' ') + ', '
          + "Hardware size:" + line[54:60].replace('|', ' ') + ', '
          + "Protocol size:" + line[60:66].replace('|', ' ') + ', '
          + "Opcode:" + line[66:72].replace('|', ' ') + ', '
          + "Sender MAC address:" + line[72:90].replace('|', ' ') + ', '
          + "Sender IP address:" + line[90:102].replace('|', ' ') + ', '
          + "Target MAC address:" + line[102:120].replace('|', ' ') + ', '
          + "Target IP address:" + line[120:132].replace('|', ' ') + ', ')


# Process the first 64 bytes of the stp packet
def parse_stp(line):
    print(line)
    print("Destination Hardware Address:" + line[:18].replace('|', ' ') + ', '
          + "Source Hardware Address:" + line[18:36].replace('|', ' ') + ', '
          + "Length:" + line[36:42].replace('|', ' ') + ', '
          + "DSAP:" + line[42:45].replace('|', ' ') + ', '
          + "SSAP:" + line[45:48].replace('|', ' ') + ', '
          + "Control field:" + line[48:51].replace('|', ' ') + ', '
          + "Protpcol Identifier:" + line[51:57].replace('|', ' ') + ', '
          + "Protpcol Version Identifier:" + line[57:60].replace('|', ' ') + ', '
          + "BPDU Type:" + line[60:63].replace('|', ' ') + ', '
          + "BPDU flags:" + line[63:66].replace('|', ' ') + ', '
          + "Root Identifier:" + line[66:90].replace('|', ' ') + ', '
          + "Root Path Cost:" + line[90:102].replace('|', ' ') + ', '
          + "Bridge Identifier:" + line[102:126].replace('|', ' ') + ', '
          + "Port identifier:" + line[126:132].replace('|', ' ') + ', '
          + "Message Age:" + line[132:138].replace('|', ' ') + ', '
          + "Hello Time:" + line[138:144].replace('|', ' ') + ', '
          + "Forward Delay:" + line[144:150].replace('|', ' ') + ', ')


def main():
    # file = 'dataset1.pcap'
    file = input('Please enter your file path:')
    pcap = open(file, 'r')
    lines = pcap.readlines()
    line_number = 0
    all_packets = []
    lens = []
    for line in lines:
        line_number += 1
        # print("Line number: {}, {}".format(line_number, line))
        if line_number % 4 == 2:
            packet = Packet()
            # packet.snd = line
            packet.timestamp = line[:16]

        if line_number % 4 == 3:
            # packet.third = line
            # packet length
            lens.append(len(line[6:-1].replace('|', '')) / 2)
            if line[42:47] == '08|00' or line[42:47] == '08|06':
                packet.layer2 = '802.2'
                if line[42:47] == '08|00':
                    packet.layer3 = 'IPV4'

                    if line[75:77] == '02':
                        packet.layer4 = 'IGMP'
                        if line[120:122] == '16':
                            parse_igmp16(line[5:])
                        if line[108:110] == '11':
                            parse_igmp11(line[5:])
                    elif line[75:77] == '01':
                        packet.layer4 = 'ICMP'
                        parse_icmp(line[5:])
                    elif line[75:77] == '06':
                        packet.layer4 = 'TCP'
                        parse_tcp(line[5:])
                    elif line[75:77] == '11':
                        packet.layer4 = 'UDP'
                        parse_udp(line[5:])
                if line[42:47] == '08|06':
                    packet.layer3 = 'ARP'
                    parse_arp(line[5:])
            else:
                packet.layer2 = '802.3'
                if line[66:68] == '00':
                    packet.layer3 = 'STP'
                    parse_stp(line[5:])
            all_packets.append(packet)

    # mark the timestamp of first packet
    last = None
    l8022, l8023, arp, icmp, igmp, ipv4, tcp, udp, stp = 0, 0, 0, 0, 0, 0, 0, 0, 0

    for pakt in all_packets:
        # print(pakt)
        if pakt.layer2 == '802.2':
            l8022 += 1
        if pakt.layer1 == '802.3':
            l8023 += 1
        if pakt.layer3 == 'ARP':
            arp += 1
        if pakt.layer3 == 'IPV4':
            ipv4 += 1
        if pakt.layer3 == 'STP':
            stp += 1
        if pakt.layer4 == 'IGMP':
            igmp += 1
        if pakt.layer4 == 'ICMP':
            icmp += 1
        if pakt.layer4 == 'TCP':
            tcp += 1
        if pakt.layer4 == 'UDP':
            udp += 1

        print("timestamp is: " + pakt.timestamp)

        if last is None:
            print("First packet does not have delta time.\n")
            last = pakt.timestamp
            continue
        else:
            delta_time = datetime.datetime.strptime(pakt.timestamp[:-4] + pakt.timestamp[-3:],
                                                    '%H:%M:%S,%f') - datetime.datetime.strptime(
                last[:-4] + last[-3:], '%H:%M:%S,%f')
        last = pakt.timestamp
        print("Delta time from last packet: {} seconds\n".format(delta_time.total_seconds()))

    print("number of packets is " + str(len(all_packets)))
    print("Protocol distribution:")
    print("802.2:{}, 802.3:{}, arp:{}, icmp:{}, igmp:{}, ipv4:{}, tcp:{}, udp:{}, stp:{}".format(l8022, l8023, arp,
                                                                                                 icmp, igmp, ipv4, tcp,
                                                                                                 udp, stp))
    print("Max size packet in terms of bytes is: " + str(max(lens)))
    print("Min size packet in terms of bytes is: " + str(min(lens)))
    print("Average size packet in terms of bytes is: " + str(sum(lens) / len(lens)))


if __name__ == '__main__':
    main()
