# Copyright 2016 Google Inc. All rights reserved.
#
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

"""Authorizes an IP address for access to Cloud SQL
"""

import yaml


def GenerateEmbeddableYaml(yaml_string):
    # This function takes a string in YAML format and produces
    # an equivalent YAML representation that can be
    # inserted into another YAML document.
    yaml_object = yaml.load(yaml_string)
    dumped_yaml = yaml.dump(yaml_object, default_flow_style=True)
    return dumped_yaml


def GenerateConfig(context):
    return """
resources:
  - type: sqladmin.v1beta4.instance
    name: %(name)s
    properties:
      region: %(sql-region)s
      databaseVersion: "MYSQL_5_7"
      settings:
        tier: db-n1-standard-1
        activationPolicy: ALWAYS
        ipConfiguration:
          ipv4Enabled: True
""" % {"sql-region": context.properties["sql-region"],
       "name": context.properties["name"],
       "address": context.properties["address"]}

