# Census6Pentachora
Census of all 4-manifolds with up to six 4-simplices.

The census has been created in Regina version 6.0.1.
To obtain it run in the Regina terminal the command:
```
tricensus -4 -t 6 -f -o -i -s out.sig
```
or look at https://regina-normal.github.io/docs/man-tricensus.html for more informations.

The classification has been done using a sphere recognition heuristic implemented in polymake.
For the classification we used polymake version 4.0 but everything should work for polymake version 3.2 or higher.
For detail on how to install polymake and getting started: https://polymake.org/doku.php

For more information on the heuristic and on the census classification: https://arxiv.org/abs/1405.3848

The repository is organized as follows:

-Each directory, 2Pentachora, 4Pentachora and 6Pentachora contains the isomorphism signature of the complexes with 2,4 or 6 pentachora respectively.
  Inside each directory you will find the isomorphism signatures in different file, depending if the examples are PL-spheres, non sphere or if we have not been able   to classify them.

-The script ReginaToPolymake.py can be used to read a isomorphism signature and create a list of facets of its second barycentric subdivision in a file readable in polymake. For more information on the final format: https://arxiv.org/pdf/1605.05057.pdf

To use the script simply run on your terminal (after having installed Regina): 
```
regina-python ReginaToPolymake.py gALLQQaaddefdfefHbgaxaBbHbzbfazbgafa sphere.facets
```
where gALLQQaaddefdfefHbgaxaBbHbzbfazbgafa should be substituted by the isomorphism signature that you want to analyze and sphere.facets is the name of the file you want to store the facets list in. 

Subsequently you can load the data in polymake using 
```
polymake -a topaz
$p=load_data("sphere.facets");
$q=new SimplicialComplex(INPUT_FACES=>$p);
```
If you want to verify that a complex is a sphere, we suggest running:
```
print random_discrete_morse($q,rounds=>10);
```
if in at least one round the vector (1,0,0,0,1) is found this is a sufficient condition for the simplicial complex to be a PL-sphere.

To verify that a complex is not a sphere, run
```
print $q->HOMOLOGY;
```
and check that the homology is not spherical.

In polymake is also available the command:
```
print $q->SPHERE;
```
but without any preprocessing on the simplicial complex and depending on the polymake version it could take a considerable amount of time and resources.

Alternatively you can also easily access the example through the Regina interface by selecting File→Import→Isomorphism Signature List. 
