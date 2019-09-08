#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `icenlp_bridge` package."""

import os
import unittest

from icenlp_bridge import init, parse

_SKIP = os.environ.get('ICENLP_DISABLE_TEST') == 'true'


class TestIcenlp_bridge(unittest.TestCase):
    """Tests for `icenlp_bridge` package."""

    def test_failed_init(self):
        with self.assertRaises(Exception):
            init('localhost', 4321)

    @unittest.skipIf(_SKIP, 'IceNLP server not running')
    def test_init(self):
        init('localhost', 1234)

    @unittest.skipIf(_SKIP, 'IceNLP server not running')
    def test_parse(self):
        init('localhost', 1234)
        result = parse('Áframhaldandi úrkoma í dag')
        self.assertIn('Áframhaldandi', result)
