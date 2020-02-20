import math as m

class Interp:
    def step(t):
        return 0 if t<.5 else 1
    def lin(t):
        return t
    def smooth(t):
        return t*t*(3 - 2*t)
    def smooth5(t):
        return t*t*t*(10 + (-15 + 6*t)*t)
    def sine(t):
        return .5-m.cos(t*m.pi)/2
    
    def clamp(x):
        return 0 if x<0 else 1 if x>1 else x
    def lerp(x, y, t):
        return (y-x)*t + x
    def unlerp(x, y, t):
        return (t-x)/(y-x)
class Keyframe:
    def __init__(self, time, interp=Interp.lin, **vars):
        self.time = time
        self.interp = interp
        self.vars = vars
    def addNext(self, other):
        self.next = other
    
    def setVars(self, time):
        globals().update(self.vars)
    def interpVars(self, time):
        t = Interp.unlerp(self.time, self.next.time, time)
        vars = {}
        for k, v in self.vars.items():
            if k in self.next.vars:
                vars[k] = Interp.lerp(self.vars[k], self.next.vars[k], t)
        globals().update(vars) 
class Animation:
    pass

if __name__ == '__main__':
    while 1:
        code = input('>>> ')
        try:
            exec(code)#execute
        except Exception as e:#error
            print(str(type(e)), ': ', e, sep='')
        else:#success
            try:
                res = eval(code)#result of operation
            except:#no operation
                pass
            else:#success
                if res != None:
                    print(repr(res))