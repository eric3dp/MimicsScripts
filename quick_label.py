import trimatic


size = 100

entity = trimatic.create_cylinder_axis([0,0,0],[0,0,1], size, size)

cyl = trimatic.convert_analytical_to_mesh(entity)
trimatic.delete(entity)

textspot = [0,size*-1, size/2]

trimatic.quick_label(entity=cyl,text="ACH24-195\nTest", point=textspot,direction=[1,0,0])

size = size/2

entity = trimatic.create_cylinder_axis([0,0,0],[0,0,1], size*2.1, size)
cyl = trimatic.convert_analytical_to_mesh(entity)
trimatic.delete(entity)
