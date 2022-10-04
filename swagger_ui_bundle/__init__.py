#!/usr/bin/env python

import os

__author__ = "Daniel Grossmann-Kavanagh"
__version__ = '0.0.10'


def get_path(rel):
    return os.path.join(
        os.path.abspath(os.path.dirname(os.path.realpath(__file__))), rel
    )


swagger_ui_2_2_10_path = get_path("vendor/swagger-ui-2.2.10")

swagger_ui_3_52_0_path = get_path("vendor/swagger-ui-3.52.0")

swagger_ui_4_14_2_path = get_path("vendor/swagger-ui-4.14.2")

# latest major versions
swagger_ui_2_path = swagger_ui_2_2_10_path
swagger_ui_3_path = swagger_ui_3_52_0_path
swagger_ui_4_path = swagger_ui_4_14_2_path

# default to swagger 3
swagger_ui_path = swagger_ui_3_path
