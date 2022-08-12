# coding: utf-8

import os
import platform
import requests
import subprocess

FFMPEG_DOWNLOAD_URL = 'http://bmc.byr.cool/assets/ffmpeg-win32.exe'
FFMPEG_SAVE_PATH = os.path.join('bin', 'ffmpeg.exe')

ffmpeg_cmd = 'ffmpeg'
# 在这里填入你使用语言对应的文件夹名
language = 'C_CPP'


def check_ffmpeg() -> bool:
    try:
        subprocess.call([ffmpeg_cmd, '-version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except:
        return False


def hint_for_unix(os_name: str):
    HELP_TEXT = {
        'Darwin': 'brew install ffmpeg',
        'Linux': 'sudo <package manager> install ffmpeg',
    }
    print('检测到你使用的是类Unix操作系统，请直接使用包管理器安装ffmpeg')
    print('可能的安装命令：{}'.format(HELP_TEXT[os_name]))
    exit(1)


def install_ffmpeg_for_win():
    resp = requests.get(FFMPEG_DOWNLOAD_URL, stream=True)
    total_size = resp.headers.get('content-length')
    if resp.status_code != 200:
        print('无法下载ffmpeg.exe，请检查网络连接或者联系管理员')
        exit(1)
    with open(FFMPEG_SAVE_PATH, 'wb') as foo:
        if total_size is None:
            foo.write(resp.content)
        else:
            dl = 0
            total_size = int(total_size)
            for data in resp.iter_content(chunk_size=4096):
                dl += len(data)
                foo.write(data)
                done = int(50 * dl / total_size)
                print("\r[%s%s] %d%%" % ('=' * done, ' ' * (50 - done), int(dl / total_size * 100)), end='')
            print()
    print('成功拉取ffmpeg到{}'.format(FFMPEG_SAVE_PATH))

def get_ffmpeg_h264_encoder(ffmpeg_cmd: str):
    out = subprocess.run([ffmpeg_cmd, '-encoders'], capture_output=True)
    if 'libx264' in out.stdout.decode():
        return 'libx264'
    else:
        return 'libopenh264'
    

def convert_gif_to_mp4(ffmpeg_cmd: str, gif_path: str, mp4_path: str):
    if not os.path.exists(gif_path):
        print('{}不存在，请检查路径'.format(gif_path))
        exit(1)
    encoder = get_ffmpeg_h264_encoder(ffmpeg_cmd)
    try:
        subprocess.call([ffmpeg_cmd, '-hide_banner', '-loglevel', 'error', '-y', '-i', gif_path,
                     '-qp', '0', '-s', '512x512', '-vcodec', encoder, '-r', '50', '-b:v',
                     '12M', mp4_path])
        print('成功转换{}到{}'.format(gif_path, mp4_path))
    except subprocess.CalledProcessError as exec:
        print('转换失败，请检查ffmpeg错误')
        print('Exit Code: {}'.format(exec.returncode))
        print('Error: {}'.format(exec.output))


ffmpeg_installed = check_ffmpeg()
if ffmpeg_installed:
    print('已检测到安装了ffmpeg，直接使用系统ffmpeg生成mp4')
else:
    print('没有检测到系统ffmpeg。', end='')
    system_str = platform.system()
    if system_str == 'Windows':
        if not os.path.exists('bin/'): os.mkdir('bin')
        ffmpeg_cmd = FFMPEG_SAVE_PATH
        if not check_ffmpeg():
            print('检测到Windows操作系统，准备自动拉取GPL ffmpeg')
            install_ffmpeg_for_win()
        else:
            print('检测到{}'.format(FFMPEG_SAVE_PATH))
    elif system_str == 'Linux' or system_str == 'Darwin':
        hint_for_unix(system_str)
    else:
        print('不支持的操作系统"{}"，请联系赛事举办方取得支持'.format(system_str))
        exit(1)

if language == '':
    print('请设置language变量')
    exit(1)

convert_gif_to_mp4(ffmpeg_cmd, os.path.join(language, 'result.gif'), os.path.join(language, 'result.mp4'))
