from theano import tensor
from theano.tensor.slinalg import kron
import warnings

warnings.warn(
        "theano modules are deprecated and will be removed in release 0.7",
        stacklevel=3)
deprecation_warning.already_displayed = True