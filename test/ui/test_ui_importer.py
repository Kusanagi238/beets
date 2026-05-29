# This file is part of beets.
# Copyright 2016, Adrian Sampson.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

"""Tests the TerminalImportSession. The tests are the same as in the

test_importer module. But here the test importer inherits from
``TerminalImportSession``. So we test this class, too.
"""

import pytest

from beets.test.helper import TerminalImportMixin
from test import test_importer


class _UITestBase:
    @pytest.fixture(autouse=True)
    def _io(self, io):
        pass


class TestNonAutotaggedImport(
    _UITestBase, TerminalImportMixin, test_importer.TestNonAutotaggedImport
):
    pass


class TestImport(_UITestBase, TerminalImportMixin, test_importer.TestImport):
    pass


class TestImportSingleton(
    _UITestBase, TerminalImportMixin, test_importer.TestImportSingleton
):
    pass


class TestImportTracks(
    _UITestBase, TerminalImportMixin, test_importer.TestImportTracks
):
    pass


class TestImportCompilation(
    _UITestBase, TerminalImportMixin, test_importer.TestImportCompilation
):
    pass


class TestImportExisting(
    _UITestBase, TerminalImportMixin, test_importer.TestImportExisting
):
    pass


class TestChooseCandidate(
    _UITestBase, TerminalImportMixin, test_importer.TestChooseCandidate
):
    pass


class TestGroupAlbumsImport(
    _UITestBase, TerminalImportMixin, test_importer.TestGroupAlbumsImport
):
    pass


class TestGlobalGroupAlbumsImport(
    _UITestBase, TerminalImportMixin, test_importer.TestGlobalGroupAlbumsImport
):
    pass
