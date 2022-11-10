# standard library imports
import socket
import time
from pathlib import Path
from threading import Lock, Thread

# third-party imports
import pytest

# local imports
import tmrl.config.config_constants as cfg
import tmrl.config.config_objects as cfg_obj
from tmrl.envs import GenericGymEnv
from tmrl.networking import RolloutWorker, Server
from tmrl.util import partial


def test_server():
    Server()


@pytest.mark.parametrize("standalone", [(True), (False)])
def test_rollout_worker(standalone):
    rw = RolloutWorker(env_cls=partial(GenericGymEnv, id="real-time-gym-v0", gym_kwargs={"config": cfg_obj.CONFIG_DICT}),
                       actor_module_cls=cfg_obj.POLICY,
                       sample_compressor=cfg_obj.SAMPLE_COMPRESSOR,
                       device='cuda' if cfg.PRAGMA_CUDA_INFERENCE else 'cpu',
                       server_ip=cfg.SERVER_IP_FOR_WORKER,
                       max_samples_per_episode=cfg.RW_MAX_SAMPLES_PER_EPISODE,
                       model_path=cfg.MODEL_PATH_WORKER,
                       obs_preprocessor=cfg_obj.OBS_PREPROCESSOR,
                       crc_debug=cfg.CRC_DEBUG,
                       standalone=standalone)  # test with False
