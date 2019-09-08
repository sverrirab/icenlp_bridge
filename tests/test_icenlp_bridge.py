#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `icenlp_bridge` package."""


import unittest

from icenlp_bridge import init, parse


class TestIcenlp_bridge(unittest.TestCase):
    """Tests for `icenlp_bridge` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        init()

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_parse1(self):
        result = parse('Áframhaldandi úrkoma í dag')
        self.assertIn('Áframhaldandi', result)

    def test_parse2(self):
        result = parse('Grindhvalirnir 62 sem syntu upp í fjöru við Ytra Lón á Langanesi í gæreru nú allir dauðir.')
        self.assertIn('Langanesi', result)
