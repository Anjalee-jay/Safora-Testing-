import subprocess
import sys
from pathlib import Path


def run_test(script_name):
    """Run a single test script and report results."""
    print(f"\n{'='*60}")
    print(f"Running: {script_name}")
    print(f"{'='*60}\n")
    
    try:
        result = subprocess.run(
            [sys.executable, script_name],
            cwd=Path(__file__).parent,
            capture_output=False,
            timeout=300
        )
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        print(f"✗ Test {script_name} timed out after 5 minutes")
        return False
    except Exception as e:
        print(f"✗ Error running test: {str(e)}")
        return False


def main():
    """Run all tests in the suite."""
    print("\n" + "="*60)
    print("SAFORA SELENIUM TEST SUITE")
    print("="*60)
    
    tests = [
        "test_safora.py",           # Basic homepage test
        "test_contact_form.py",     # Contact form automation
    ]
    
    results = {}
    
    for test in tests:
        script_path = Path(__file__).parent / test
        if script_path.exists():
            results[test] = run_test(test)
        else:
            print(f"✗ Test file not found: {test}")
            results[test] = False
    
    # Print summary
    print("\n" + "="*60)
    print("TEST SUITE SUMMARY")
    print("="*60)
    
    total = len(results)
    passed = sum(1 for v in results.values() if v)
    failed = total - passed
    
    for test_name, result in results.items():
        status = "✓ PASSED" if result else "✗ FAILED"
        print(f"{test_name:<30} {status}")
    
    print("-"*60)
    print(f"Total: {total} | Passed: {passed} | Failed: {failed}")
    print("="*60 + "\n")
    
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
