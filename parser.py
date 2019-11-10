#
# Parser for settings file
#
def ParseLine(lst=None):
    result = [lst[0],0.,0.,0.]
    for element in lst[1:]:
        if "erg" in element:
            result[1] = float(element.strip().replace("erg=", ''))
        elif "its" in element:
            result[2] = float(element.strip().replace("its=", ''))
        elif "fwhm" in element:
            result[3] = float(element.strip().replace("fwhm=", ''))
        else:
          raise NameError("unknown indetifier")
    return result

def ParseBkg(lst=None):
    result = [lst[0],0.,0.,0.,0.]
    for element in lst[1:]:
        if "ep1" in element:
            result[1] = float(element.strip().replace("ep1=", ''))
        elif "ep2" in element:
            result[2] = float(element.strip().replace("ep2=", ''))
        elif "a" in element:
            result[3] = float(element.strip().replace("a=", ''))
        elif "b" in element:
            result[4] = float(element.strip().replace("b=", ''))
        else:
          print(element)
          raise NameError("unknown indetifier")
    return result

def ParseRange(lst=None):
    result = ['range',0.,0.,0.,0]
    for element in lst[1:]:
        if "emin" in element:
            result[1] = float(element.strip().replace("emin=", ''))
        elif "emax" in element:
            result[2] = float(element.strip().replace("emax=", ''))
        elif "nch" in element:
            result[3] = int(element.strip().replace("nch=", ''))
        elif "time" in element:
            result[4] = float(element.strip().replace("time=", ''))
        else:
          raise NameError("unknown indentifier")
    return result

def Parse(line=None):
    lst = line[:line.find("#")].lower().rstrip().split()
    if lst == []: return None
    if "line" in lst[0]:
        return ParseLine(lst)
    if "bkg" in lst[0]:
        return ParseBkg(lst)
    elif "range" in lst[0]:
        return ParseRange(lst)
    else:
      raise ValueError("Setting file contain else variables!")
class LineParameters(object):
    def __init__(self, parameters=None):
        self.intensity = parameters[1]
        self.energy    = parameters[0]
        self.sigma     = parameters[2] / 2.355
    def __call__(self):
        return (self.intensity, self.energy, self.sigma)


class Settings(object):
    def __init__(self, file=None):
        parsed = [Parse(line) for line in open(file, "r")
                      if line.strip() != '' and Parse(line) != None]
        self.psd = parsed
        self.lines = []
        for element in parsed:
            if 'line' in element[0]:
                self.lines.append(LineParameters(element[1:]))
            elif 'range' in element[0]:
                self.emin = element[1]
                self.emax = element[2]
                self.nbins = element[3]
            elif 'bkg' in element[0]:
                self.bkg_exp1   = element[1]
                self.bkg_exp2   = element[2]
                self.bkg_a      = element[3]
                self.bkg_b      = element[4]

    def __call__(self):
        return self.psd
    def __str__(self):
        return str(self.psd)