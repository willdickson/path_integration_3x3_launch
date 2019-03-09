import os

class Config:

    def __init__(self,nodenum=1):
        self.basename = 'delta_video'
        self.directory = '~/devel/devel_{}/data'.format(nodenum)
        self.topics = ['/multi_tracker/{}/delta_video'.format(nodenum),]
        self.record_length_hours = 1

        self.directory = os.path.expanduser(self.directory)
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
