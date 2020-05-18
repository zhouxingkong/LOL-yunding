#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `winiobinary` package."""

import winiobinary
import os.path


def test_data_dir():
    """
    Test if data dirs are exists
    """

    # Ensure WinIo 2.0 exists
    assert os.path.exists(os.path.join(
        winiobinary.get_data_dir('2.0'), 'WINIO.VXD'))

    # Ensure WinIo 3.0 exists
    assert os.path.exists(os.path.join(
        winiobinary.get_data_dir(), 'WinIo64.sys'))
