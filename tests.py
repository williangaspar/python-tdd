from unittest import TestLoader, TextTestRunner, TestSuite
import test_linear
import test_format_math

if __name__ == "__main__":

    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(test_linear.TestLienar),
        loader.loadTestsFromTestCase(test_format_math.TestFormatting),
    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)
