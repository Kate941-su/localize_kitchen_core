"""
Examples of different ways to import sdk_list with relative paths
"""
import unittest
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ImportExamples(unittest.TestCase):
    """Examples of different import methods"""
    
    def test_method1_absolute_import(self):
        """Method 1: Absolute import (recommended for tests)"""
        from src.sdk.sdk import sdk_list
        expected = ['xcode', 'android_studio', 'flutter', 'react_native']
        self.assertEqual(sdk_list, expected)
    
    def test_method2_package_import(self):
        """Method 2: Package import"""
        from src.sdk import sdk_list
        expected = ['xcode', 'android_studio', 'flutter', 'react_native']
        self.assertEqual(sdk_list, expected)
    
    def test_method3_module_import(self):
        """Method 3: Module import"""
        import src.sdk.sdk as sdk_module
        expected = ['xcode', 'android_studio', 'flutter', 'react_native']
        self.assertEqual(sdk_module.sdk_list, expected)
    
    def test_method4_relative_import(self):
        """Method 4: Relative import (requires running as module)"""
        # This only works when running: python -m test.import_examples
        try:
            from ..src.sdk.sdk import sdk_list
            expected = ['xcode', 'android_studio', 'flutter', 'react_native']
            self.assertEqual(sdk_list, expected)
        except ImportError:
            # Skip this test if relative import doesn't work
            self.skipTest("Relative import requires running as module")
    
    def test_method5_dynamic_import(self):
        """Method 5: Dynamic import"""
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "sdk", 
            os.path.join(os.path.dirname(os.path.dirname(__file__)), "src", "sdk", "sdk.py")
        )
        sdk_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(sdk_module)
        
        expected = ['xcode', 'android_studio', 'flutter', 'react_native']
        self.assertEqual(sdk_module.sdk_list, expected)

if __name__ == '__main__':
    unittest.main()

