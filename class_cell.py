'''definition of a class wafer, containing the location and the value of the cells'''

from db_extractor import blob2list

class wafer:

    cell_list = []

    def __init__(self):
        self.x = []
        self.y = []
        self.value = []
        self.cell_list.append(self)


    def add_cell(self, x, y, spec_extracted, spec_analyser):

        if spec_extracted == None:
            spec_wlen = None
        else:
            spec_wlen = blob2list(spec_extracted)


        if x!=None and y!=None and spec_wlen != None :

            spec = spec_wlen[1:len(spec_extracted):2]
            wlen = spec_wlen[0:-1:2]

        else:
            spec = None
            wlen = None

        if spec_analyser(wlen, spec) != None:

            self.x.append(x)
            self.y.append(y)
            self.value.append(spec_analyser(wlen,spec)[0])


    def amplitude(self):
        M = max(p for p in self.value)
        m = min(p for p in self.value)
        # python doesn't round well
        ampli = (M-m)/1.9999
        midl = (M+m)/2
        return(ampli,midl,M,m)

