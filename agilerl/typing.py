from typing import Union, Dict, List, Tuple, Any
import torch
from numpy.typing import ArrayLike
from torch.optim import Optimizer
from torch.nn import Module
from accelerate.optimizer import AcceleratedOptimizer
import gymnasium as gym
from gymnasium import spaces

from agilerl.protocols import EvolvableAlgorithm
from agilerl.modules.configs import MlpNetConfig, CnnNetConfig

ArrayOrTensor = Union[ArrayLike, torch.Tensor]
TensorDict = Dict[str, torch.Tensor]
TensorTuple = Tuple[torch.Tensor, ...]
ArrayDict = Dict[str, ArrayOrTensor]
ArrayTuple = Tuple[ArrayLike, ...]
NetConfigType = Dict[str, Any]
KernelSizeType = Union[int, Tuple[int, ...]]
GymSpaceType = Union[spaces.Space, List[spaces.Space]]
GymEnvType = Union[str, gym.Env, gym.vector.VectorEnv]

NumpyObsType = Union[ArrayLike, ArrayDict, ArrayTuple]
TorchObsType = Union[torch.Tensor, TensorDict, TensorTuple]
ObservationType = Union[NumpyObsType, TorchObsType]
InfosDict = Dict[str, Dict[str, Any]]
MaybeObsList = Union[List[ObservationType], ObservationType]
ExperiencesType = Tuple[ObservationType, ...]

DeviceType = Union[str, torch.device]
OptimizerType = Union[Optimizer, AcceleratedOptimizer]
NetworkType = Union[Module, List[Module], Tuple[Module, ...]]
PopulationType = List[EvolvableAlgorithm]
ConfigType = Union[Union[MlpNetConfig, CnnNetConfig], Dict[str, Any]]
StateDict = Union[Dict[str, Any], List[Dict[str, Any]]]