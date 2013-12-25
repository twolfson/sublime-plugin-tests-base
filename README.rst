sublime-plugin-tests-base
=========================

.. image:: https://travis-ci.org/twolfson/sublime-plugin-tests-base.png?branch=master
   :target: https://travis-ci.org/twolfson/sublime-plugin-tests-base
   :alt: Build Status

Base layer for testing and assertion frameworks against `Sublime Text`_

This is part of the `sublime-plugin-tests`_ project, a full testing framework for `Sublime Text`_

.. _`sublime-plugin-tests`: https://github.com/twolfson/sublime-plugin-tests
.. _`Sublime Text`: http://sublimetext.com/

For supported versions and FAQs, please consult `sublime-plugin-tests`_.

Getting Started
---------------
Install the module with: ``pip install sublime_plugin_tests_base``

Then, write your tests:

.. code:: python

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

.. code:: bash

    $ # Run tests via nosetests
    $ nosetests
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.076s

    OK

Documentation
-------------
_(Coming soon)_

Examples
--------
_(Coming soon)_

Contributing
------------
In lieu of a formal styleguide, take care to maintain the existing coding style. Add unit tests for any new or changed functionality. Test via ``nosetests``.

Donating
--------
Support this project and `others by twolfson`_ via `gittip`_.

.. image:: https://rawgithub.com/twolfson/gittip-badge/master/dist/gittip.png
   :target: `gittip`_
   :alt: Support via Gittip

.. _`others by twolfson`:
.. _gittip: https://www.gittip.com/twolfson/

Unlicense
---------
As of Dec 23 2013, Todd Wolfson has released this repository and its contents to the public domain.

It has been released under the `UNLICENSE`_.

.. _UNLICENSE: https://github.com/twolfson/sublime-plugin-tests-base/blob/master/UNLICENSE
