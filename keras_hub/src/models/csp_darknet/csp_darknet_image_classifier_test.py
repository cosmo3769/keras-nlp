# Copyright 2023 The KerasHub Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import numpy as np
import pytest

from keras_hub.src.models.csp_darknet.csp_darknet_backbone import (
    CSPDarkNetBackbone,
)
from keras_hub.src.models.csp_darknet.csp_darknet_image_classifier import (
    CSPDarkNetImageClassifier,
)
from keras_hub.src.tests.test_case import TestCase


class CSPDarkNetImageClassifierTest(TestCase):
    def setUp(self):
        # Setup model.
        self.images = np.ones((2, 16, 16, 3), dtype="float32")
        self.labels = [0, 3]
        self.backbone = CSPDarkNetBackbone(
            stackwise_num_filters=[2, 16, 16],
            stackwise_depth=[1, 3, 3, 1],
            include_rescaling=False,
            block_type="basic_block",
            image_shape=(16, 16, 3),
        )
        self.init_kwargs = {
            "backbone": self.backbone,
            "num_classes": 2,
            "activation": "softmax",
        }
        self.train_data = (
            self.images,
            self.labels,
        )

    def test_classifier_basics(self):
        pytest.skip(
            reason="TODO: enable after preprocessor flow is figured out"
        )
        self.run_task_test(
            cls=CSPDarkNetImageClassifier,
            init_kwargs=self.init_kwargs,
            train_data=self.train_data,
            expected_output_shape=(2, 2),
        )

    @pytest.mark.large
    def test_saved_model(self):
        self.run_model_saving_test(
            cls=CSPDarkNetImageClassifier,
            init_kwargs=self.init_kwargs,
            input_data=self.images,
        )
