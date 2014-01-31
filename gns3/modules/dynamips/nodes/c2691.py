# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Dynamips c2691 router implementation.
"""

from .router import Router


class C2691(Router):
    """
    Dynamips c2691 router.

    :param server: GNS3 server instance
    """

    def __init__(self, server):
        Router.__init__(self, server, platform="c2691")

        self._platform_settings = {"ram": 128,
                                   "nvram": 112,
                                   "disk0": 16,
                                   "disk1": 0,
                                   "iomem": 5,
                                   "clock_divisor": 8}

        # merge platform settings with the generic ones
        self._settings.update(self._platform_settings)

    def __str__(self):

        return "Router c2691"

    @staticmethod
    def symbolName():

        return "Router c2691"
