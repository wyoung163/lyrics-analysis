from oslo_config import cfg
from . import default, cors, music_sites

CONF = cfg.CONF

conf_modules = [
    default,
    cors,
    music_sites
]

def configure(conf=None, config_file_path="/etc/lyrics/lyrics.conf"):
    if conf is None:
        conf = CONF

    for module in conf_modules:
        module.register_opts(conf)

    CONF(['--config-file=' + config_file_path], project='lyrics')