#!/bin/bash
# Script to run FOAF RDF validation tests

echo "Installing dependencies..."
pip3 install -q -r requirements.txt

echo ""
echo "Running FOAF RDF validation test..."
python3 test_foaf_validation.py

exit $?
