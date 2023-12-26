import argparse
import json
import logging
import signal
import subprocess
import os
import argparse
from time import sleep


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)    







# 首次安装模式，实际命令：softsecdroidbot -a <apk_path> -policy none
# 授予特定权限需要使用-special_perm指定，具体权限以android.permission.CAMERA为例
def first_install(config):
    
    app_path = config['app_path']

    global droidbot_process
    
    try:
        if config["special_perm"]:
            droidbot_process = subprocess.Popen(["softsecdroidbot", "-a",app_path,"-special_perm",config["special_perm"],"-policy","none"], stdout=subprocess.PIPE)
        else:
            droidbot_process = subprocess.Popen(["softsecdroidbot", "-a",app_path,"-policy","none"], stdout=subprocess.PIPE)

        logger.info("Softsec-droidbot started in first_start mode.")
        
        # 测试结束任务函数
        sleep(50)
        stop_droidbot()
        
        droidbot_process.wait()  # 等待子进程结束

    except subprocess.CalledProcessError as e:
        logger.error(f"Error during first install mode: {e}")
    except KeyboardInterrupt:
        logger.info("Ctrl+C detected. Stopping DroidBot.")
        droidbot_process.terminate()  # 终止子进程
        droidbot_process.wait()  # 等待子进程结束
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")

    


# 静默模式，实际命令：softsecdroidbot -a <apk_path> -is_quiet -scripts <touch_agree.json>
# 授予特定权限需要使用-special_perm指定，具体权限以android.permission.CAMERA为例

def quiet(config):
    app_path = config['app_path']
    global droidbot_process
 
    try:
        if config["special_perm"]:
            droidbot_process = subprocess.Popen(["softsecdroidbot", "-a",app_path,"-special_perm",config["special_perm"],"-is_quiet","-script","C:/Users/Administrator/Desktop/softsec-droidbot/script_samples/touch_agree.json"], stdout=subprocess.PIPE)
        else:
            droidbot_process = subprocess.Popen(["softsecdroidbot", "-a",app_path,"-is_quiet","-script","C:/Users/Administrator/Desktop/softsec-droidbot/script_samples/touch_agree.json"], stdout=subprocess.PIPE)

        logger.info("softsecdroidbot started in quiet mode.")

        # 测试结束任务函数
        sleep(100)
        stop_droidbot()

        
        droidbot_process.wait()  # 等待子进程结束

    except subprocess.CalledProcessError as e:
        logger.error(f"Error starting DroidBot in quiet mode: {e}")
    except KeyboardInterrupt:
        logger.info("Ctrl+C detected. Stopping DroidBot.")
        droidbot_process.terminate()  # 终止子进程
        droidbot_process.wait()  # 等待子进程结束
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")


def stop_droidbot():
    global droidbot_process

    if droidbot_process is not None:
        try:
            logger.info("DroidBot is ready to stop.")
            droidbot_process.send_signal(signal.CTRL_C_EVENT)  # 向子进程发送 Ctrl+C 信号，droidbot响应KeyboardInterrupt
            droidbot_process.wait()  # 等待子进程结束
            logger.info("DroidBot stop finished.")

        except Exception as e:
            return f"Error terminating DroidBot: {e}"
    else:
        return "DroidBot process not found."




## config 包含：APK路径，mode模式(quiet,first_install)，special_perm授予特定权限

def main():


    # special_perm 参数说明：指定某权限，安装时自动授予

    config = {
        "app_path":r"C:/Users/Administrator/Desktop/YogaNow_1.4.10.apk",
        "mode":"first_install",
        "special_perm":"android.permission.CAMERA"
    }
    
    droidbot_process =None




    if config['mode'] == 'first_install':
        first_install(config)
    elif config['mode'] == 'quiet':
        quiet(config)





    

if __name__ == '__main__':
    main()
    
