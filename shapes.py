class Circle:
	def __init__(self,radius):
		self.radius=radius
		

	def Area_of_a_circle(self):
		radius=self.radius
		A=(3.142)*(radius*radius)
		return(A)

	def circumference_of_a_circle(self):
		radius=self.radius
		C=2*3.142*(radius)
		return(C)
				

class Square:
	def __init__(self,side):
		self.side=side

	def Area_of_a_square(self):
		side=self.side
		Area_of_a_square=side*side
		return(Area_of_a_square)

	def Perimeter_of_a_square(self):
		side=self.side
		Perimeter_of_a_square=4*side
		return(Perimeter_of_a_square)


class Rectangle:
	def __init__(self,w,l):
		self.w=w
		self.l=l		


	def Area_of_a_rectangle(self):
		w=self.w
		l=self.l
		Area_of_a_rectangle=w*l
		return(Area_of_a_rectangle)

	def Perimeter_of_a_rectangle(self):
		w=self.w
		l=self.l
		Perimeter_of_a_rectangle=(2*w)+(2*l)
		return(Perimeter_of_a_rectangle)


class Sphere:
	def __init__(self,radius):
		self.radius=radius

	def Sphere_SA(self):
		radius=self.radius
		Sphere_SA=4*3.142*radius*radius
		return(Sphere_SA)

	def Sphere_Volume(self):
		radius=self.radius
		Sphere_Volume=(4/33.142)*(radius*radius*radius)
		return(Sphere_Volume)	














