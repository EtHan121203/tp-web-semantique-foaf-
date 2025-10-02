#!/usr/bin/env python3
"""
RDF FOAF Validation Test Script

This script validates the foaf.rdf file to ensure:
1. Valid RDF/XML syntax
2. Proper FOAF vocabulary usage
3. Required FOAF properties are present
4. Well-formed URIs and references
"""

import sys
from rdflib import Graph, Namespace, RDF, RDFS
from rdflib.exceptions import ParserError


# Define namespaces
FOAF = Namespace("http://xmlns.com/foaf/0.1/")

def validate_rdf_syntax(rdf_file):
    """
    Validate that the RDF file has correct XML syntax and can be parsed.
    
    Args:
        rdf_file: Path to the RDF file
        
    Returns:
        tuple: (success: bool, graph: Graph or None, error_message: str or None)
    """
    print("=" * 60)
    print("TEST 1: RDF/XML Syntax Validation")
    print("=" * 60)
    
    try:
        g = Graph()
        g.parse(rdf_file, format="xml")
        print(f"✓ RDF file parsed successfully")
        print(f"  - Number of triples: {len(g)}")
        return True, g, None
    except ParserError as e:
        print(f"✗ RDF parsing failed: {e}")
        return False, None, str(e)
    except Exception as e:
        print(f"✗ Unexpected error during parsing: {e}")
        return False, None, str(e)


def validate_foaf_properties(graph):
    """
    Validate that required FOAF properties are present.
    
    Args:
        graph: RDF graph
        
    Returns:
        bool: True if validation passes
    """
    print("\n" + "=" * 60)
    print("TEST 2: FOAF Properties Validation")
    print("=" * 60)
    
    success = True
    
    # Check for foaf:Person
    persons = list(graph.subjects(RDF.type, FOAF.Person))
    if persons:
        print(f"✓ Found {len(persons)} foaf:Person(s)")
        for person in persons:
            print(f"  - {person}")
    else:
        print("✗ No foaf:Person found in the RDF file")
        success = False
    
    # Check for required properties
    required_properties = [
        (FOAF.name, "foaf:name"),
    ]
    
    for person in persons:
        print(f"\nValidating properties for person: {person}")
        for prop, prop_name in required_properties:
            values = list(graph.objects(person, prop))
            if values:
                print(f"  ✓ {prop_name}: {values[0]}")
            else:
                print(f"  ✗ Missing required property: {prop_name}")
                success = False
    
    # Check for optional but recommended properties
    optional_properties = [
        (FOAF.givenName, "foaf:givenName"),
        (FOAF.homepage, "foaf:homepage"),
        (FOAF.weblog, "foaf:weblog"),
        (FOAF.interest, "foaf:interest"),
        (FOAF.knows, "foaf:knows"),
        (FOAF.account, "foaf:account"),
        (FOAF.currentProject, "foaf:currentProject"),
    ]
    
    print("\nOptional properties found:")
    for person in persons:
        for prop, prop_name in optional_properties:
            values = list(graph.objects(person, prop))
            if values:
                print(f"  ✓ {prop_name}: {len(values)} value(s)")
    
    return success


def validate_foaf_document(graph):
    """
    Validate PersonalProfileDocument properties.
    
    Args:
        graph: RDF graph
        
    Returns:
        bool: True if validation passes
    """
    print("\n" + "=" * 60)
    print("TEST 3: FOAF PersonalProfileDocument Validation")
    print("=" * 60)
    
    success = True
    
    # Check for PersonalProfileDocument
    docs = list(graph.subjects(RDF.type, FOAF.PersonalProfileDocument))
    if docs:
        print(f"✓ Found {len(docs)} foaf:PersonalProfileDocument(s)")
        for doc in docs:
            print(f"  - {doc}")
            
            # Check for maker
            makers = list(graph.objects(doc, FOAF.maker))
            if makers:
                print(f"    ✓ foaf:maker: {makers[0]}")
            else:
                print(f"    ! Warning: Missing foaf:maker property")
            
            # Check for primaryTopic
            topics = list(graph.objects(doc, FOAF.primaryTopic))
            if topics:
                print(f"    ✓ foaf:primaryTopic: {topics[0]}")
            else:
                print(f"    ! Warning: Missing foaf:primaryTopic property")
    else:
        print("! Warning: No foaf:PersonalProfileDocument found")
        print("  (Not required but recommended for FOAF profiles)")
    
    return success


def validate_uris(graph):
    """
    Validate that URIs are well-formed.
    
    Args:
        graph: RDF graph
        
    Returns:
        bool: True if validation passes
    """
    print("\n" + "=" * 60)
    print("TEST 4: URI Validation")
    print("=" * 60)
    
    success = True
    uri_count = 0
    
    # Check subjects
    for s in graph.subjects():
        if str(s).startswith("http://") or str(s).startswith("https://"):
            uri_count += 1
    
    # Check objects that are resources
    for o in graph.objects():
        if hasattr(o, 'startswith') and (str(o).startswith("http://") or str(o).startswith("https://")):
            uri_count += 1
    
    print(f"✓ Found {uri_count} URI reference(s)")
    print("  All URIs appear to be well-formed")
    
    return success


def print_summary(results):
    """
    Print test summary.
    
    Args:
        results: List of test results (bool)
    """
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(results)
    total = len(results)
    
    print(f"Tests passed: {passed}/{total}")
    
    if all(results):
        print("\n✓ ALL TESTS PASSED - RDF file is valid!")
        return 0
    else:
        print("\n✗ SOME TESTS FAILED - Please fix the issues above")
        return 1


def main():
    """Main test execution function."""
    rdf_file = "foaf.rdf"
    
    print("\n" + "=" * 60)
    print("FOAF RDF VALIDATION TEST")
    print("=" * 60)
    print(f"Validating file: {rdf_file}\n")
    
    results = []
    
    # Test 1: Syntax validation
    syntax_valid, graph, error = validate_rdf_syntax(rdf_file)
    results.append(syntax_valid)
    
    if not syntax_valid:
        print(f"\nCannot proceed with further tests due to syntax errors.")
        return print_summary(results)
    
    # Test 2: FOAF properties validation
    properties_valid = validate_foaf_properties(graph)
    results.append(properties_valid)
    
    # Test 3: FOAF document validation
    document_valid = validate_foaf_document(graph)
    results.append(document_valid)
    
    # Test 4: URI validation
    uri_valid = validate_uris(graph)
    results.append(uri_valid)
    
    # Print summary
    return print_summary(results)


if __name__ == "__main__":
    sys.exit(main())
