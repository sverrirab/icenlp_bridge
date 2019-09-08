#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `icenlp_bridge` package."""

import os
import unittest

from icenlp_bridge import init, parse


class TestIcenlp_bridge(unittest.TestCase):
    """Tests for `icenlp_bridge` package."""

    @unittest.skipIf(os.environ.get('TRAVIS') == 'true', 'IceNLP server not running')
    def test_init(self):
        init('localhost', 1234)

    def test_failed_init(self):
        print('TRAVIS:', os.environ.get('TRAVIS'))
        with self.assertRaises(Exception) as context:
            init('localhost', 4321)

    @unittest.skipIf(os.environ.get('TRAVIS') == 'true', 'IceNLP server not running')
    def test_parse(self):
        init('localhost', 1234)
        result = parse('Áframhaldandi úrkoma í dag')
        self.assertIn('Áframhaldandi', result)
