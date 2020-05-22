# Copyright 2019 Open Source Robotics Foundation

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import em
import pkgutil

from .extensions import name_to_argument
from .core import RockerExtension

class SshServer(RockerExtension):
    @staticmethod
    def get_name():
        return 'ssh_server'

    def __init__(self):
        self._env_subs = None
        self.name = SshServer.get_name()

    def get_environment_subs(self, cliargs={}):
        if not self._env_subs:
            self._env_subs = {}
        return self._env_subs

    def get_snippet(self, cliargs):
        snippet = pkgutil.get_data('rocker', 'templates/%s_snippet.Dockerfile.em' % self.name).decode('utf-8')
        return em.expand(snippet, self.get_environment_subs())

    @staticmethod
    def register_arguments(parser, defaults={}):
        parser.add_argument(name_to_argument(SshServer.get_name()),
            action='store_true',
            default=defaults.get(SshServer.get_name(), False),
            help="Installs and configures an SSH server inside the container")
