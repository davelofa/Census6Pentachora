# Census6Pentachora
Census of all 4-manifolds with up to six 4-simplices

The census has been created through the tricensus command in Regina and classified using a sphere recognition heuristic implemented in polymake.
For more information on the heuristic and on the census classification: https://arxiv.org/abs/1405.3848

The repository is organized as follows:

-Each directory, 2Pentachora, 4Pentachora and 6Pentachora contains the isomorphism signature of the complexes with 2,4 or 6 pentachora respectively.
  Inside each directory you will find the isomorphism signatures in different file, depending if the examples are PL-spheres, non sphere or if we have not been able   to classify them.

-The script ReginaToPolymake.py can be used to read a isomorphism signature and create a list of facets of its second barycentric subdivision in a file readable in polymake.

To use the script simply run on your terminal: regina-python ReginaToPolymake.py gALLQQaaddefdfefHbgaxaBbHbzbfazbgafa sphere.facets

where gALLQQaaddefdfefHbgaxaBbHbzbfazbgafa should be substituted by the isomorphism signature that you want to analyze and sphere.facets is the name of the file you want to store the facets list in. Subsequently you can load the data in polymake using $p=load_data("sphere.facets").
Alternatively you can easily access the example through the Regina interface by selecting File→Import→Isomorphism Signature List. 
