class Packet():

    def __init__(self):
        self.snd = ''
        self.third = ''
        self.timestamp = ''
        self.layer1 = ''
        self.layer2 = ''
        self.layer3 = ''


    def __str__(self):
        return '{snd}{frth}{timestamp}\n{layer1}\n{layer2}\n{layer3}'.format(snd=self.snd, third=self.third, timestamp=self.timestamp, layer1=self.layer1, layer2=self.layer2, layer3=self.layer3)



