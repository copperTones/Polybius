import pyglet
import math
# from pyglet.window import key
from copy import deepcopy

# window = pyglet.window.Window()#(width=800, height=600)

class hypercube:
	def __init__(self, dim, rad):
		if type(dim) is not int:
			raise TypeError('dimensions is not an int')
		if dim < 1:
			raise ValueError('dimensions cannot be less than 1')
		
		self._ang = math.pi/dim
		self._rad = rad/2
		#return (_hyperP(dim, window.width/2, window.height/2), _hyperC(dim), _hyperL(dim))

	def points(n, x, y):
		if n > 0:#stop infinite
			dx, dy = r*math.sin(a*n + b), r*math.cos(a*n + b)
			return _hyperP(n-1, x+dx, y+dy) + _hyperP(n-1, x-dx, y-dy)
		else:
			return [x, y]
	def lines(dim):
		if not dim:
			return [0, 0]
		
		list = [0, 1]#start w/ 0,1
		for n in range(1, dim):#each iteration, add:
			pow = 2**n
			list += [x+pow for x in list]#copy of list +2**n
			for i in range(pow):#every 0...(2**n-1),+2**n
				list += (i, i+pow)
		
		return list
	def colors(dim):
		if dim == 0:
			return [1, 1, 1]
		
		col = [0, 0, 0]
		for n in range(0, dim):
			col += [i+1 for i in col]#col[i] = col[i-2**n] + 1
		
		return [i/dim for i in col]
	
	def draw()
	
	b, s, f = 0, 1, 1
	def loop(dt):
		global b, s
		b += dt * s
	# pyglet.clock.schedule_interval(loop, 1/60)
	def flip(dt):
		global s, f
		s += dt*f
		if not -1 <= s <= 1:
			s = f#clamp
			pyglet.clock.unschedule(flip)