# Copyright (c) 2015 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
Constants used by the hooks.

"""
import sys

## PYC FILE PATH
HOOK_PATH = "%s/shotgun/studio/custom/hooks/tk-multi-workfiles2/v0.0.1/{hook_file}" % {'win32':'r:', 'darwin':'/mnt' }[sys.platform]
