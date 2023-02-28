from SPARQLWrapper import SPARQLWrapper, CSV as fmt
from io import StringIO
import pandas as pd

endpoint = "http://localhost:8080/sparql"
sparql = SPARQLWrapper(endpoint)

def query_endpoint(q):
    sparql.setQuery(q)
    sparql.setReturnFormat(fmt)
    results = sparql.query().convert()
    csv = results.decode()

    return pd.read_csv(StringIO(csv))

q = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX : <https://github.com/glaubernunes/ontology-for-bariatric-surgery/raw/main/ontology-for-bariatric-surgery.owl#>

SELECT  ?habito (COUNT(?pessoa) AS ?n) WHERE {
	?pessoa :OBAS_0000173 ?h .
	?h rdfs:label ?habito .
} GROUP BY ?habito
"""

results = query_endpoint(q)
print(results.to_string())
