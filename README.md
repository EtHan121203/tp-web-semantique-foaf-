# FOAF RDF Validation Test

This repository contains a FOAF (Friend of a Friend) RDF profile and a validation test script to ensure the RDF file is properly formatted and contains valid FOAF data.

## Files

- `foaf.rdf` - The FOAF RDF profile
- `test_foaf_validation.py` - Python script to validate the RDF file
- `requirements.txt` - Python dependencies
- `index.html` - Web page linking to the FOAF profile

## Running the Validation Test

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Installation

1. Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

### Running the Test

#### Option 1: Using the convenience script (recommended)

```bash
./run_validation.sh
```

This script will automatically install dependencies and run the validation test.

#### Option 2: Running directly

```bash
python3 test_foaf_validation.py
```

### What the Test Validates

The validation script performs the following checks:

1. **RDF/XML Syntax Validation**: Ensures the RDF file is well-formed XML and can be parsed
2. **FOAF Properties Validation**: Verifies that required FOAF properties (like `foaf:name`) are present for all `foaf:Person` entities
3. **PersonalProfileDocument Validation**: Checks for the presence and proper configuration of `foaf:PersonalProfileDocument`
4. **URI Validation**: Ensures all URIs in the document are well-formed

### Expected Output

When the RDF file is valid, you should see:

```
============================================================
FOAF RDF VALIDATION TEST
============================================================
Validating file: foaf.rdf

============================================================
TEST 1: RDF/XML Syntax Validation
============================================================
✓ RDF file parsed successfully
  - Number of triples: XX

[... additional test results ...]

============================================================
TEST SUMMARY
============================================================
Tests passed: 4/4

✓ ALL TESTS PASSED - RDF file is valid!
```

## FOAF Profile Information

The FOAF profile (`foaf.rdf`) contains structured metadata about a person according to the FOAF vocabulary, enabling interoperability in the Semantic Web context. It includes:

- Personal information (name, given name)
- Web identity (homepage, weblog)
- Academic information (current project, school homepage)
- Interests (Semantic Web, Linked Data, Web Development)
- Online accounts (GitHub)
- Social connections (knows relationships)

## References

- [FOAF Specification](http://xmlns.com/foaf/spec/)
- [RDFLib Documentation](https://rdflib.readthedocs.io/)
- [Semantic Web](https://www.w3.org/standards/semanticweb/)
