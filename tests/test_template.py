# ******************************************************************************
#
# template-python, python project template
#
# Copyright 2023-2024 Jeremy A Gray <gray@flyquackswim.com>.
#
# All rights reserved.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# ******************************************************************************

"""Template tests."""

from template import Template


def test_repr_should_work():
    """Should be default ``repr``."""
    assert repr(Template()) == "Template()"
