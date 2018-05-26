import sys
sys.path.append("../metal")

import unittest

import numpy as np
import torch

from synthetics.generate import generate_single_task_unipolar
from metal.label_model.label_model import LabelModel


class LabelModelTest(unittest.TestCase):

    def test_single_task_basic(self):
        # Generate unipolar L for single task
        N, M = 10000, 20
        L, Y, accs = generate_single_task_unipolar(N, M)

        # Initialize label model
        model = LabelModel()

        # Train label model
        model.train(L)


if __name__ == '__main__':
    unittest.main()