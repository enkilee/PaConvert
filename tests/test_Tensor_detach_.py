# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
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

obj = APIBase("torch.Tensor.detach_")


# Tensor.detach_ throws unexpected exception, refer to: https://github.com/PaddlePaddle/Paddle/issues/57303
def _test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[1.0, 1.0, 1.0],
                        [2.0, 2.0, 2.0],
                        [3.0, 3.0, 3.0]], requires_grad=True)
        linear = torch.nn.Linear(3, 4)
        y = linear(x)
        y.detach_()
        """
    )
    obj.run(pytorch_code, ["y"])


def _test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[1.0, 1.0, 1.0]], requires_grad=True)
        x.detach_()
        """
    )
    obj.run(pytorch_code, ["x"])
