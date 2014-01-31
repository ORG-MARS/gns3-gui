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
Dynamips module implementation.
"""

import socket
from gns3.qt import QtCore
from gns3.servers import Servers
from ..module import Module
from .nodes.router import Router
from .nodes.c1700 import C1700
from .nodes.c2600 import C2600
from .nodes.c2691 import C2691
from .nodes.c3600 import C3600
from .nodes.c3725 import C3725
from .nodes.c3745 import C3745
from .nodes.c7200 import C7200
from .nodes.cloud import Cloud
from .nodes.ethernet_switch import EthernetSwitch
from .nodes.ethernet_hub import EthernetHub
from .nodes.frame_relay_switch import FrameRelaySwitch
from .nodes.atm_switch import ATMSwitch
from .settings import DYNAMIPS_SETTINGS, DYNAMIPS_SETTING_TYPES


class Dynamips(Module):

    def __init__(self):
        Module.__init__(self)

        self._settings = {}
        self._ios_images = {}
        self._servers = []

        # load the settings and IOS images.
        self._loadSettings()
        self._loadIOSImages()

    def _loadSettings(self):

        # load the settings
        settings = QtCore.QSettings()
        settings.beginGroup(self.__class__.__name__)
        for name, value in DYNAMIPS_SETTINGS.items():
            self._settings[name] = settings.value(name, value, type=DYNAMIPS_SETTING_TYPES[name])
        settings.endGroup()

    def _saveSettings(self):

        # save the settings
        settings = QtCore.QSettings()
        settings.beginGroup(self.__class__.__name__)
        for name, value in self._settings.items():
            settings.setValue(name, value)
        settings.endGroup()

    def _loadIOSImages(self):

        # load the settings
        settings = QtCore.QSettings()
        settings.beginGroup("IOS_images")

        # load the IOS images
        size = settings.beginReadArray("ios_image")
        for index in range(0, size):
            settings.setArrayIndex(index)
            path = settings.value("path", "")
            image = settings.value("image", "")
            startup_config = settings.value("image", "")
            platform = settings.value("platform", "")
            chassis = settings.value("chassis", "")
            idlepc = settings.value("idlepc", "")
            ram = settings.value("ram", 128, type=int)
            server = settings.value("server", "local")

            key = "{server}:{image}".format(server=server, image=image)
            self._ios_images[key] = {"path": path,
                                     "image": image,
                                     "startup-config": startup_config,
                                     "platform": platform,
                                     "chassis": chassis,
                                     "idlepc": idlepc,
                                     "ram": ram,
                                     "server": server}

        settings.endArray()
        settings.endGroup()

    def _saveIOSImages(self):

        # save the settings
        settings = QtCore.QSettings()
        settings.beginGroup("IOS_images")
        settings.remove("")

        # save the IOS images
        settings.beginWriteArray("ios_image", len(self._ios_images))
        index = 0
        for ios_image in self._ios_images.values():
            settings.setArrayIndex(index)
            for name, value in ios_image.items():
                settings.setValue(name, value)
            index += 1
        settings.endArray()
        settings.endGroup()

    def addServer(self, server):

        self._servers.append(server)
        server.send_notification("dynamips.settings", self._settings)

    def removeServer(self, server):

        self._servers.remove(server)

    def servers(self):

        return self._servers

    def iosImages(self):

        return self._ios_images

    def setIOSImages(self, new_ios_images):

        self._ios_images = new_ios_images.copy()
        self._saveIOSImages()

    def settings(self):

        return self._settings

    def setSettings(self, settings):

        params = {}
        for name, value in settings.items():
            if self._settings[name] != value:
                params[name] = value

        if params:
            for server in self._servers:
                server.send_notification("dynamips.settings", params)

        self._settings.update(settings)
        self._saveSettings()

    def createNode(self, node_class):

        servers = Servers.instance()
        server = servers.localServer()

        if not server.connected:
            try:
                server.connect()
            except socket.error as e:
                print("COULD NOT CONNECT TO SERVER!!")
                print(e)
                return

        self.addServer(server)
        return node_class(server)

    def _allocateIOSImage(self, node):

        platform = node.settings()["platform"]
        for ios_image in self._ios_images.values():
            if ios_image["platform"] == platform:
                return ios_image

    def setupNode(self, node):

        if isinstance(node, Router):
            ios_image = self._allocateIOSImage(node)
            #node.setup(ios_image)
            node.setup("/home/grossmj/Documents/IOS images/c3725-adventerprisek9-mz.124-15.T14.image", 128)
        else:
            node.setup()

    @staticmethod
    def nodes():
        """
        Returns all the node classes supported by this module.

        :returns: list of classes
        """

        return [C1700, C2600, C2691, C3600, C3725, C3745, C7200, Cloud, EthernetSwitch, EthernetHub, FrameRelaySwitch, ATMSwitch]

    @staticmethod
    def preferencePages():
        """
        :returns: QWidget object list
        """

        from .pages.dynamips_preferences_page import DynamipsPreferencesPage
        from .pages.ios_router_preferences_page import IOSRouterPreferencesPage
        return [DynamipsPreferencesPage, IOSRouterPreferencesPage]

    @staticmethod
    def instance():
        """
        Singleton to return only on instance of Dynamips.

        :returns: instance of Dynamips
        """

        if not hasattr(Dynamips, "_instance"):
            Dynamips._instance = Dynamips()
        return Dynamips._instance
