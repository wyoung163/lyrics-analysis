from oslo_config import cfg
import sys

GROUP_NAME = __name__.split('.')[-1]

ALL_OPTS = [
    cfg.StrOpt('url', default='https://music-sites/')
]

def register_opts(conf):
    conf.register_opt(ALL_OPTS, group=GROUP_NAME)