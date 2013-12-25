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

Travis CI integration
^^^^^^^^^^^^^^^^^^^^^
We support both Sublime Text 2 and 3 via Travis CI.

Please consult `sublime-plugin-tests#travis-ci-integration`_ for the most up-to-date information.

.. _`sublime-plugin-tests#travis-ci-integration`: https://github.com/twolfson/sublime-plugin-tests#travis-ci-integration

Documentation
-------------
``sublime-plugin-tests-base`` consists of two pieces: test framework code (outside Sublime Text) and test helpers (inside Sublime Text).

The test framework code is run in your normal development environment (e.g. where ``nosetests`` lives). The test helpers live inside of Sublime text to make your testing life easier.

Test framework
^^^^^^^^^^^^^^
Base(auto_kill_sublime=False)
"""""""""""""""""""""""""""""
Class for running enclosed tests inside of Sublime. It handles capturing and returning errors.

- auto_kill_sublime ``Boolean`` - If true, this will close Sublime Text automatically when the test completes.
    - This is useful for headless environments which are using a synchronous Sublime Text (e.g. Sublime Text 2)

base.directory
""""""""""""""
Folder where tests are run. This can be used for writing relatively imported files.

run_test(action_str)
""""""""""""""""""""
Run code within the context of Sublime Text. This will capture any **synchronous** errors that occur. To clarify, if you use ``sublime.set_timeout``, we cannot report back the error.

- action_str ``String`` - Code to run within the context of Sublime Text. This should be making assertions against views as the data will not be available in the ``result``.

**Returns:**

- result ``Dictionary`` - Container for results
    - success ``Boolean`` - If there were no errors, ``True``. Otherwise, ``False``.
    - meta_info ``String`` - Formatted traceback from the error that occurred.

Test helpers
^^^^^^^^^^^^
utils.scratch_view.ScratchView
""""""""""""""""""""""""""""""
This assists with creating/tearing down/manipulating views.

Please consult `sublime-plugin-tests#utilsscratch_viewscratchview`_ for the most up-to-date information.

.. _`sublime-plugin-tests#utilsscratch_viewscratchview`: https://github.com/twolfson/sublime-plugin-tests#utilsscratch_viewscratchview

Architecture
------------
Please consult `sublime-plugin-tests#architecture`_ for the most up-to-date information.

.. _`sublime-plugin-tests#architecture`: https://github.com/twolfson/sublime-plugin-tests#architecture

Contributing
------------
In lieu of a formal styleguide, take care to maintain the existing coding style. Add unit tests for any new or changed functionality. Test via ``./test.sh``.

If you would like to headlessly run the tests, this repository can be used with `Vagrant`_.

..

    Currently, it is only configured for Sublime Text 3.

.. _Vagrant: http://vagrantup.com/

.. code:: bash

    $ vagrant up
    [default] Importing base box 'precise64'...
    ...
    $ vagrant ssh st2 # Sublime Text 3
    $ # Use `st3` for Sublime Text 2
    vagrant@precise64:~$ cd /vagrant
    vagrant@precise64:/vagrant$ ./test.sh
    ..
    ----------------------------------------------------------------------
    Ran 2 tests in 2.957s

    OK

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
