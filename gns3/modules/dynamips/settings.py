# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 GNS3 Technologies Inc.
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
Default Dynamips settings.
"""

import sys
import os

# default path to Dynamips executable
if sys.platform.startswith("win"):
    DEFAULT_DYNAMIPS_PATH = "dynamips.exe"
elif sys.platform.startswith('darwin'):
    if hasattr(sys, "frozen"):
        DEFAULT_DYNAMIPS_PATH = os.path.join(os.getcwdu(), "../Resources/dynamips-0.2.10-OSX.intel64.bin")
    else:
        DEFAULT_DYNAMIPS_PATH = os.path.join(os.getcwdu(), "dynamips-0.2.10-OSX.intel64.bin")
else:
    DEFAULT_DYNAMIPS_PATH = "dynamips"

DYNAMIPS_SETTINGS = {
    "path": DEFAULT_DYNAMIPS_PATH,
    "base_hypervisor_port": 7200,
    "base_console_port": 2101,
    "base_aux_port": 2501,
    "allocate_hypervisor_per_device": True,
    "memory_usage_limit_per_hypervisor": 1024,
    "allocate_hypervisor_per_ios_image": True,
    "base_udp_port": 10001,
    "udp_incrementation_per_hypervisor": 100,
    "ghost_ios_support": True,
    "jit_sharing_support": False,
    "sparse_memory_support": True,
    "mmap_support": True,
}

DYNAMIPS_SETTING_TYPES = {
    "path": str,
    "base_hypervisor_port": int,
    "base_console_port": int,
    "base_aux_port": int,
    "allocate_hypervisor_per_device": bool,
    "memory_usage_limit_per_hypervisor": int,
    "allocate_hypervisor_per_ios_image": bool,
    "base_udp_port": int,
    "udp_incrementation_per_hypervisor": int,
    "ghost_ios_support": bool,
    "jit_sharing_support": bool,
    "sparse_memory_support": bool,
    "mmap_support": bool,
}
