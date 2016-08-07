# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <gogogo.vm@gmail.com>
"""

from __future__ import absolute_import

import dataproperty

from ._function import str_datetime_converter
from ._function import dateutil_datetime_converter
from ._text_writer import SourceCodeTableWriter


class PythonCodeTableWriter(SourceCodeTableWriter):
    """
    Concrete class of a table writer for Python code (nested list) format.

    :Examples:

        :ref:`example-python-code-table-writer`
    """

    @property
    def support_split_write(self):
        return True

    def __init__(self):
        super(PythonCodeTableWriter, self).__init__()

        self.table_name = u""
        self._prop_extractor.inf_value = 'float("inf")'
        self._prop_extractor.nan_value = 'float("nan")'

    def write_table(self):
        """
        |write_table| with Python nested list variable definition format.

        :raises pytablewriter.EmptyTableDataError:
            If the |header_list| and the |value_matrix| is empty.

        .. note::

            - |None| is written as ``None``
            - |inf| is written as ``float("inf")'``
            - |nan| is written as ``float("nan")'``
        """

        self._verify_property()

        if self.is_datetime_instance_formatting:
            self._prop_extractor.datetime_converter = dateutil_datetime_converter
        else:
            self._prop_extractor.datetime_converter = str_datetime_converter

        self.inc_indent_level()
        super(PythonCodeTableWriter, self).write_table()
        self.dec_indent_level()

    def _get_opening_row_item_list(self):
        if dataproperty.is_not_empty_string(self.table_name):
            return [self.variable_name + u" = ["]

        return u"["

    def _get_closing_row_item_list(self):
        return u"]"
