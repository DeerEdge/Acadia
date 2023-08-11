from semanticscholar import SemanticScholar
sch = SemanticScholar()
results = sch.search_paper('Computing Machinery and Intelligence')
print(f'{results.total} results.', f'First occurrence: {results[0].title}.')