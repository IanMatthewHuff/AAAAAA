import os

class Assembler:
    ''' Main class for the art assembler '''
    def __init__(self):
        ''' Constructor '''

    def listBlocks(self):
        ''' List out all available blocks '''
        blocksFiles = os.listdir('./Blocks')
        print(str(blocksFiles))
