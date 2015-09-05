# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://bitbucket.org/ned/coveragepy/src/default/NOTICE.txt

"""A test base class for tests based on gold file comparison."""

import os
import sys

from tests.coveragetest import CoverageTest

from coverage.test_helpers import change_dir    # pylint: disable=unused-import
from tests.test_farm import clean
# Import helpers, eventually test_farm.py will go away.
from tests.test_farm import (       # pylint: disable=unused-import
    compare, contains, doesnt_contain, contains_any,
)


class CoverageGoldTest(CoverageTest):
    """A test based on gold files."""

    run_in_temp_dir = False

    def setUp(self):
        super(CoverageGoldTest, self).setUp()
        self.chdir(self.root_dir)
        # Modules should be importable from the current directory.
        sys.path.insert(0, '')

    def output_dir(self, the_dir):
        """Declare where the output directory is.

        The output directory is deleted at the end of the test, unless the
        COVERAGE_KEEP_OUTPUT environment variable is set.

        """
        self.addCleanup(self.cleanup_output_dir, the_dir)

    def cleanup_output_dir(self, the_dir):
        """Clean up the output directory of the test."""
        if not os.environ.get("COVERAGE_KEEP_OUTPUT"):      # pragma: partial
            clean(the_dir)
