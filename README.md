# Census6Pentachora
Census of all 4-manifolds with six 4-simplices

The census has been created through the tricensus command in Regina and classified using a sphere recognition heuristic implemented in polymake.
For more information on the heuristic and on the census classification: https://arxiv.org/abs/1405.3848

The repository is organized as follows:

-spheres.sig, not_spheres.sig, unknown.sig contain the ismorphism signatures of the examples that are PL-spheres, non sphere and that we have not been able to classify respectively.

-The script ReginaToPolymake.py can be used to read a isomorphism signature and create a list of facets of its second barycentric subdivision in a file readable in polymake.

To use the script simply run on your terminal: regina-python ReginaToPolymake.py gALLQQaaddefdfefHbgaxaBbHbzbfazbgafa sphere.facets

where gALLQQaaddefdfefHbgaxaBbHbzbfazbgafa should be substituted by the isomorphism signature that you want to analyze and sphere.facets is the name of the file you want to store the facets list in. Subsequently you can load the data in polymake using $p=load_data("sphere.facets").
Alternatively you can easily access the example through the Regina interface by selecting File→Import→Isomorphism Signature List. 
