import pyglet
from hypercube import hypercube

@window.event
def on_draw():
	window.clear()
	
	points, colors, lines = hypercube(D, 100)
	pyglet.graphics.draw_indexed(len(points)//2, pyglet.gl.GL_LINES,
		lines,
		('v2f', points),
		('c3f', colors))

pyglet.app.run()