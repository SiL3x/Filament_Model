# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 23:08:36 2014

@author: mutant
"""

import numpy as np
import matplotlib.pyplot as plt


###############################################
#   Define Functions
###############################################

def create_mesh( mesh_size , box_x , box_y , box_z):
    mesh = np.zeros(( int(box_z/mesh_size) , int(box_y/mesh_size) , int(box_x/mesh_size)) ) 
    return( mesh )
    
def add_mesh( mesh ):    
    out_array = np.zeros(np.shape(mesh)[1:])
    for i in range( 0 , np.shape(mesh)[0] ):
        out_array = np.add( out_array , mesh[i] )
    return(out_array)

def add_rnd_cylinder( r_range , theta_range , omega_range , input_mesh):
    radius = np.random.random_integers(r_range[0], r_range[1])
    xy_range = [ np.shape(input_mesh)[2]-2*radius, np.shape(input_mesh)[1]-2*radius ]
    origin_xy = [np.random.random_integers( 0 , xy_range[0]) , np.random.random_integers( 0 , xy_range[1])]
    max_radius = radius
    cylinder_cut = np.zeros((max_radius , max_radius))
    for i in range( 0 , max_radius ):
        circle_part = [1]*int(np.around(np.sqrt(radius**2 - i**2)))
        zero_part = [0]*(max_radius-len(circle_part))
        cylinder_cut[i]= circle_part+zero_part
    cylinder_cut = np.concatenate((np.rot90(cylinder_cut),cylinder_cut),axis=0)
    cylinder_cut = np.concatenate((np.rot90(np.rot90(cylinder_cut)),cylinder_cut),axis=1)
    for i in range(0,np.shape(input_mesh)[0]):        
        input_mesh[i,origin_xy[0]:origin_xy[0]+2*radius , origin_xy[1]:origin_xy[1]+2*radius]=cylinder_cut
    
    return input_mesh
            
    
    
    
print "Yo1"

###############################################
#   Program
###############################################

mesh_xyz    = [70,70,70]
volume      = mesh_xyz[0]*mesh_xyz[1]*mesh_xyz[2]

test_mesh   = create_mesh(1,*mesh_xyz)

volume_fraction = 0
filament_count  = 0
while ( volume_fraction <= 0.2 ):
    test_mesh = add_rnd_cylinder( [5,10] , 0 , 0 , test_mesh)
    volume_fraction = np.sum(test_mesh)/volume
    filament_count  = filament_count + 1    
    print "Volume Fraction:",volume_fraction," Filament Count:", filament_count
    
    
print "Filament Count:", filament_count
fig1 = plt.gcf()
#title('Filament Count', filament_count)
plt.imshow( add_mesh(np.rot90(test_mesh,k=1)), cmap = plt.get_cmap('gray'), vmin = 0, vmax = 70 )
plt.show()
        