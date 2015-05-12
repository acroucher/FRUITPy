"""Runs FRUITPy unit tests."""

import unittest
import FRUIT

class FRUITPyTestCase(unittest.TestCase):

    def suite_test(self, suite, files, global_setup, 
                   global_teardown, num_modules):
        """Tests a suite against specified expected values."""
        self.assertEqual(suite.test_filenames, files)
        self.assertEqual(suite.global_setup, global_setup)
        self.assertEqual(suite.global_teardown, global_teardown)
        self.assertEqual(suite.num_test_modules, num_modules)

    def module_test(self, mod, setup, teardown, global_setup,
                    global_teardown, num_subroutines):
        """Tests a module against specified expected values."""
        self.assertEqual(mod.setup, setup)
        self.assertEqual(mod.teardown, teardown)
        self.assertEqual(mod.global_setup, global_setup)
        self.assertEqual(mod.global_teardown, global_teardown)
        self.assertEqual(len(mod.subroutines), num_subroutines)

    def subroutine_test(self, sub, name, description):
        """Tests a subroutine against specified expected values."""
        self.assertEqual(sub.name, name)
        self.assertEqual(sub.description, description)
        self.assertEqual(sub.subtype, "test")
        
    def test_adder(self):
        """Unit test for adder module."""

        files = ['adder_test.F90']
        
        suite = FRUIT.test_suite(files)
        self.suite_test(suite, files, global_setup = False, 
                        global_teardown = False, num_modules = 1)
                   
        mod = suite.test_modules[0]
        self.module_test(mod, setup = None, teardown = None, 
                         global_setup = False, global_teardown = False, 
                         num_subroutines = 5)
        self.subroutine_test(mod.subroutines[0],
                             "test_add1", "test_add1")
        self.subroutine_test(mod.subroutines[1],
                             "test_add2", "Adder test with comment")
        self.subroutine_test(mod.subroutines[2],
                             "test_add3_setup", "Adder test with setup in title")
        self.subroutine_test(mod.subroutines[3],
                             "test_teardown_test", "Adder test with teardown in title")
        self.subroutine_test(mod.subroutines[4],
                             "TEST_OLDSCHOOL", "TEST ALL CAPS, MISSING END NAME")

    def test_global_setup(self):
        """Tests global setup/ teardown module."""

        files = ['setup.F90', 'adder_test.F90']
        
        suite = FRUIT.test_suite(files)
        self.suite_test(suite, files, global_setup = True, 
                        global_teardown = True, num_modules = 2)

        mod = suite.test_modules[1]
        self.module_test(mod, setup = None, teardown = None, 
                         global_setup = False, global_teardown = False, 
                         num_subroutines = 5)

    def test_module_setup(self):
        """Tests module setup/ teardown routines."""

        files = ['adder_setup_test.F90']
        
        suite = FRUIT.test_suite(files)
        self.suite_test(suite, files, global_setup = False, 
                        global_teardown = False, num_modules = 1)

        mod = suite.test_modules[0]
        self.module_test(mod, setup = 'local_setup', teardown = 'teardown_adder', 
                         global_setup = False, global_teardown = False, 
                         num_subroutines = 2)
        self.subroutine_test(mod.subroutines[0],
                             "test_1", "test_1")
        self.subroutine_test(mod.subroutines[1],
                             "test_2", "Test 2 with setup")

if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(FRUITPyTestCase)
    unittest.TextTestRunner(verbosity = 1).run(suite)

