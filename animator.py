import math as m

class Interp:
    '''\
Class for interpolation functions and lerp-related functions.
Useful with interpolating between keyframes.'''
    def step(t):
        '''All values over .5 become 1, below returns 0'''
        return 0 if t<.5 else 1
    def lin(t):
        '''Linear function.'''
        return t
    def smooth(t):
        '''Most basic smoothstep, order 3.'''
        return t*t*(3 - 2*t)
    def smooth5(t):
        '''Order 5 smoothstep.'''
        return t*t*t*(10 + (-15 + 6*t)*t)
    def sine(t):
        '''Sinusoidal interpolation.'''
        return .5-m.cos(t*m.pi)/2
    
    def newSmooth(deg):
        '''Returns a 2n+1 order smoothstep function.'''
        def smooth(t):
            x = 0
            for k in range(deg+1):
                x += combo(deg+k, k)*combo(2*deg+1, deg-k)*(-t)**k
            return x*t**(deg+1)
        smooth.__doc__ = '''A {} order smoothstep function.'''.format(2*deg+1)
        return smooth
    
    # def clamp(x):
        # return 0 if x<0 else 1 if x>1 else x
    def lerp(x, y, t):
        '''Lerp between two values.'''
        return (y-x)*t + x
    def unlerp(x, y, t):
        '''Map value in a given range to 0...1.'''
        return (t-x)/(y-x)

class Keyframe:
    def __init__(self, time, interp=Interp.lin, **vars):
        self.time = time
        self.interp = interp
        self.vars = vars
    def __addNext(self, other):
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
    def __init__(self, loop=0, *keyf):
        keyf = sorted(keyf, lambda f: f.time)
        for i in range(len(keyf)-1):
            keyf[i].__addNext(keyf[i+1])
        loop = max(0, loop)
        if loop:
            keyf[len(keyf)-1].__addNext(keyf[0])
        
        self.keyf = keyf
        self.loop = loop
    

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