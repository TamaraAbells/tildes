# Copyright (c) 2019 Tildes contributors <code@tildes.net>
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Validation/dumping schema for group wiki pages."""

from marshmallow import Schema

from tildes.schemas.fields import Markdown, SimpleString


PAGE_NAME_MAX_LENGTH = 40


class GroupWikiPageSchema(Schema):
    """Marshmallow schema for group wiki pages."""

    page_name = SimpleString(max_length=PAGE_NAME_MAX_LENGTH)
    markdown = Markdown(max_length=1_000_000)
