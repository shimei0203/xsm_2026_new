#!/bin/bash
set -e

echo "Running CSV Cleaner validation tests..."

# First run the solution to generate clean data
bash solution/solve.sh

# Run test logic
python3 tests/test_logic.py

# Capture result
TEST_RESULT=$?

if [ $TEST_RESULT -eq 0 ]; then
    echo "✅ All tests passed"
    exit 0
else
    echo "❌ Tests failed"
    exit 1
fi