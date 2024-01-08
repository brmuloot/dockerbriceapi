import pytest
from model import IrisModel, IrisSpecies


def test_model_initialization():
    new_model = IrisModel()
    assert 'iris_model.joblib' in new_model.model_fname_
