#!/usr/bin/python

#Python and Regina script takes as input an isomorphism signature and 
#print as output a simplicial complex obtained by taking the 
#second barycentric subdvision of the complex.


#Uncomment the next line if you installed Regina through pip
#from regina import *


#Import the triangulation in Regina

t=Triangulation4(sys.argv[1])


#Take the second barycentric subdivision

t.barycentricSubdivision()
t.barycentricSubdivision()


#Print the Facet List of the simplicial complex in a polymake readable file

FacetList=[]



for i in t.pentachora() :

	vertices=[]
	
	for j in range(5):

		vertices.append(i.vertex(j).index())
	
	FacetList.append(vertices)
	
	

with open(sys.argv[2], 'w') as output:

	output.write('<?xml version="1.0" encoding="utf-8"?> \n')
	output.write('<?pm chk="5ebe4a60"?> \n \n')
	output.write('<data type="common::Array&lt;Set&lt;Int&gt;&gt;" version="3.2" xmlns="http://www.math.tu-berlin.de/polymake/#3"> \n')
	output.write(' <m> \n')
	
	for row in FacetList:
		s = " ".join(map(str, row))
      		output.write('  <v> ' + s + ' </v> \n')
        	
	output.write(' </m> \n')
	output.write('</data>')
 
    

