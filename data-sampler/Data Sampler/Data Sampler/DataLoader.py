from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://192.168.37.1:7200/repositories/Apartment134")

def load(dr):
    sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
    prefix time: <http://www.w3.org/2006/time#>.
    prefix sosa: <http://www.w3.org/ns/sosa/> .
    prefix ssn:  <http://www.w3.org/ns/ssn/> .
    prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
    prefix qudt-1-1: <http://qudt.org/1.1/schema/qudt#> .
    prefix qudt-unit-1-1: <http://qudt.org/1.1/vocab/unit#> .
    base <http://example.org/data/> .

    SELECT DISTINCT  ?p
    WHERE { ?s ?p ?o }
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(result["p"]["value"])

