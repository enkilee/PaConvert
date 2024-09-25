# Copyright (c) 2024 PaddlePaddle Authors. All Rights Reserved.
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

import textwrap

from apibase import APIBase

obj = APIBase("torch.blackman_window")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.blackman_window(5)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False, check_dtype=False)


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.blackman_window(5, dtype=torch.float64)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.blackman_window(5, dtype=torch.float64, requires_grad=True)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.blackman_window(5, dtype=torch.float64, layout=torch.strided, requires_grad=True)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.blackman_window(5, dtype=torch.float64, layout=torch.strided, device=torch.device('cpu'), requires_grad=True)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_6():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.blackman_window(5, periodic=False, dtype=torch.float64)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)
