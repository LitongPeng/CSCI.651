# CSCI.651
CSCI 651 Programming Assignment 1 – Packet Parser

Due Sunday 2-28-21 by 11:59 pm.

In this project you will write a program that takes in raw Wireshark packets and provides output that describes the details regarding the packets contained in the dataset. Your program will be tested against other datasets. For this semester we will standardize on Python 3.7 for all assignments.

In order to write a true parser, you would have to be able to understand every single type of packet and value for each header field. The good news is that you only need target the given set of packet types.

	An example of a packet from each program is shown below. These are the text-based versions with which we will be working. They can be opened in a text editor or the program itself.

Wireshark

+---------+---------------+----------+
03:09:24,762,913   ETHER
|0   |60|67|20|2c|5c|ca|9c|2a|70|01|ec|f4|08|00|45|08|00|34|3f|27|40|00|39|06|1d|c3|26|45|ee|10|c0|a8|0f|d4|00|50|c5|35|80|ad|63|3d|be|e2|f1|93|80|10|00|f5|d9|22|00|00|01|01|05|0a|be|e2|f1|92|be|e2|f1|93|

In a machine learning task we might clean up all of the data for use as features. However, for this programming assignment you need only to extract details about each packet and the collection of packets in the dataset.

Specifically, you are to produce the following details:

Dataset:	number of packets
		Protocol distribution
		Max, min and average size packet in terms of bytes

Packet:		timestamp
		Delta time from last packet
		Process the first 64 bytes of the packet – all fields and their meanings

Required packet types: 802.2, 802.3, ARP, ICMP, IGMP, IPv4, TCP, UDP, STP – additional processing may required to determine port numbers or message type.
![image](https://user-images.githubusercontent.com/60895337/109706610-2951b280-7b67-11eb-8b9d-9c39c2ba4207.png)
