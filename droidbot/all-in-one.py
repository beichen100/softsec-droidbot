import argparse

from start import parse_args
from . import input_manager
from . import input_policy
from . import env_manager
from .droidbot import DroidBot
from .droidmaster import DroidMaster


def task_send():
    opts = parse_args()

    droidbot = DroidBot(
            app_path=opts.apk_path,
            device_serial=opts.device_serial,
            is_emulator=opts.is_emulator,
            output_dir=opts.output_dir,
            # env_policy=opts.env_policy,
            env_policy=env_manager.POLICY_NONE,
            policy_name=opts.input_policy,
            random_input=opts.random_input,
            script_path=opts.script_path,
            event_interval=opts.interval,
            timeout=opts.timeout,
            event_count=opts.count,
            cv_mode=opts.cv_mode,
            debug_mode=opts.debug_mode,
            keep_app=opts.keep_app,
            keep_env=opts.keep_env,
            profiling_method=opts.profiling_method,
            grant_perm=opts.grant_perm,
            enable_accessibility_hard=opts.enable_accessibility_hard,
            master=opts.master,
            humanoid=opts.humanoid,
            ignore_ad=opts.ignore_ad,
            replay_output=opts.replay_output
    )

def device_init():

    

    droidbot.logger.info("Starting init device")
    droidbot.device.set_up()