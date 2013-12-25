# Load in unittest and test base
from unittest import TestCase
from sublime_plugin_tests_base import Base

# Define a TestCase
class TestLeftDelete(TestCase):
    def test_left_delete_single(self):
        # Each test function *must* return Python with a `run` function
        # `run` will be run inside Sublime Text. Perform your assertions etc there.
        # Run a test
        base = Base()
        result = base.run_test("""
# Use ScratchView utility provided by `sublime_plugin_tests`
from utils.scratch_view import ScratchView

def run():
  # Generate new scratch file
  scratch_view = ScratchView()
  try:
      # Update the content and selection `ab|c`
      scratch_view.set_content('abc')
      scratch_view.set_sel([(2, 2)])

      # Delete one character to the left `a|c
      scratch_view.run_command('left_delete')

      # Assert the current content
      assert scratch_view.get_content() == 'ac'
  finally:
      # No matter what happens, close the view
      scratch_view.destroy()
""")

        # Assert the test passed as expected
        self.assertEqual(result['success'], True)
