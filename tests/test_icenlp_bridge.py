#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `icenlp_bridge` package."""


import unittest

from icenlp_bridge import parse


class TestIcenlp_bridge(unittest.TestCase):
    """Tests for `icenlp_bridge` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_parse(self):
        parse('Áframhaldandi úrkoma í dag')
