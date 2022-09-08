# coding: utf-8

import argparse
import importlib
import os
import platform
from traceback import print_tb
import requests
import subprocess
from colorama import Fore, Style
import sys


def script_relative(relative_path: str) -> str:
    # 返回相对脚本路径的文件的绝对路径
    return os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), relative_path))


FFMPEG_DOWNLOAD_URL = 'https://xia.st/dists/ffmpeg.exe'
FFMPEG_FALLBACK_URLS = ['https://mimi.nekonode.com/dist/ffmpeg.exe', 'http://bmc.byr.cool/assets/ffmpeg-win32.exe']
FFMPEG_SAVE_PATH = script_relative(os.path.join('bin', 'ffmpeg.exe'))

ffmpeg_cmd = 'ffmpeg'
# 在这里填入你使用语言对应的文件夹名
language = 'C_CPP'


def print_info(msg: str, *args, **kwargs):
    print(Fore.GREEN + msg + Fore.RESET, *args, **kwargs)


def print_warning(msg: str, *args, **kwargs):
    print(Fore.YELLOW + msg + Fore.RESET, *args, **kwargs)


def print_error(msg: str, *args, **kwargs):
    print(Fore.RED + msg + Fore.RESET, *args, **kwargs)


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
    print_error('检测到你使用的是类Unix操作系统，请直接使用包管理器安装ffmpeg')
    print_error('可能的安装命令：{}'.format(HELP_TEXT[os_name]))
    exit(1)


def install_ffmpeg_for_win():
    url = FFMPEG_DOWNLOAD_URL
    resp = requests.get(url, stream=True)
    total_size = resp.headers.get('content-length')
    i = 0
    while (resp.status_code != 200 and resp.status_code != 302) and i < len(FFMPEG_FALLBACK_URLS):
        print_warning('从{}拉取ffmpeg失败，尝试备用地址'.format(url))
        url = FFMPEG_FALLBACK_URLS[i]
        resp = requests.get(url, stream=True)
        total_size = resp.headers.get('content-length')
        i += 1

    if resp.status_code != 200 and resp.status_code != 302:
        print_error('无法下载ffmpeg.exe({})，请检查网络连接或者联系管理员'.format(resp.status_code))
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
    print_info('成功拉取ffmpeg到{}'.format(FFMPEG_SAVE_PATH))


def get_ffmpeg_h264_encoder(ffmpeg_cmd: str):
    out = subprocess.run([ffmpeg_cmd, '-encoders'], capture_output=True)
    if 'libx264' in out.stdout.decode():
        return 'libx264'
    else:
        return 'libopenh264'


def convert_gif_to_mp4(ffmpeg_cmd: str, gif_path: str, mp4_path: str):
    if not os.path.exists(gif_path):
        print_error('{}不存在，请检查路径'.format(gif_path))
        exit(1)
    encoder = get_ffmpeg_h264_encoder(ffmpeg_cmd)
    try:
        subprocess.call([ffmpeg_cmd, '-hide_banner', '-loglevel', 'error', '-y', '-i', gif_path,
                         '-s', '512x512', '-pix_fmt', 'yuv420p', '-profile:v', 'main', '-vcodec', encoder, '-r', '25', '-b:v',
                         '12M', mp4_path])
        print('成功转换{}到{}'.format(gif_path, mp4_path))
    except subprocess.CalledProcessError as exec:
        print_error('转换失败，请检查ffmpeg错误')
        print_error('Exit Code: {}'.format(exec.returncode))
        print_error('Error: {}'.format(exec.output))


def encode_gif(force_download: bool = False, gif_path: str = 'result.gif', mp4_path: str = 'result.mp4'):
    global ffmpeg_cmd
    ffmpeg_installed = check_ffmpeg()
    if ffmpeg_installed and not force_download:
        print_info('已检测到安装了ffmpeg，直接使用系统ffmpeg生成mp4')
    else:
        print_error('没有检测到系统ffmpeg。', end='')
        system_str = platform.system()
        if system_str == 'Windows':
            bin_path = script_relative('./bin')
            if not os.path.exists(script_relative(bin_path)):
                os.mkdir(bin_path)
            ffmpeg_cmd = script_relative(FFMPEG_SAVE_PATH)
            if not check_ffmpeg() or force_download:
                print('检测到Windows操作系统，准备自动拉取LGPL ffmpeg')
                install_ffmpeg_for_win()
            else:
                print('检测到{}'.format(FFMPEG_SAVE_PATH))
        elif system_str == 'Linux' or system_str == 'Darwin':
            hint_for_unix(system_str)
        else:
            print_error('不支持的操作系统"{}"，请联系赛事举办方取得支持'.format(system_str))
            exit(1)

    if language == '':
        print_error('请设置language变量')
        exit(1)

    convert_gif_to_mp4(ffmpeg_cmd, gif_path, mp4_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # force-dl 强制下载ffmpeg，不管是否已经安装
    parser.add_argument('-f', '--force-dl', action='store_true', help='强制下载ffmpeg')
    # confirm 跳过覆盖确认
    parser.add_argument('-y', '--confirm', action='store_true', help='强制覆盖当前已有的gif')
    # gif gif文件路径
    parser.add_argument('-g', '--gif', type=str, help='gif文件路径', default=script_relative('./result.gif'))
    # mp4 mp4文件路径
    parser.add_argument('-m', '--mp4', type=str, help='mp4文件路径', default=script_relative('./result.mp4'))
    # 是否仅输出使用语言 language
    parser.add_argument('-l', '--language', action='store_true', help='输出当前使用语言')
    # 是否仅输出使用语言language对应的文件路径
    parser.add_argument('-s', '--source', action='store_true', help='输出当前使用语言对应的源文件目录')

    args = parser.parse_args()

    if args.language:
        print(language)
        exit(0)
    if args.source:
        join = os.path.join
        if language == 'C_CPP':
            print(join('C_CPP', 'render.h'))
        elif language == 'Java':
            print(join('Java', 'src', 'main', 'java', 'work', 'byrio', 'byrmathematicalartchallenge', 'Render.java'))
        elif language == 'Python':
            print(join('Python', 'render.py'))
        elif language == 'Rust':
            print(join('Rust', 'src', 'render.rs'))
        elif language == 'JavaScript':
            ts_path = join('JavaScript', 'src', 'ts.ts')
            js_path = join('JavaScript', 'src', 'js.js')
            with open(ts_path, 'r') as foo:
                target = ts_path if 'true' in foo.readline() else js_path
            print(target)
        exit(0)

    gif_path = os.path.abspath(args.gif)
    mp4_path = os.path.abspath(args.mp4)

    comp = importlib.import_module('{}.compile_and_run'.format(language))

    lang_path = script_relative('./{}'.format(language))

    print_info('你选择使用的语言目录：{}'.format(language))

    if os.path.exists(gif_path) and not args.confirm:
        confirm_in = input('{}已存在，是否覆盖？[y/n]'.format(gif_path))
        if confirm_in != 'y':
            print_error('退出')
            exit(1)

    # 切换工作目录到语言目录
    os.chdir(lang_path)
    sys.path.append(lang_path)

    print('开始编译...')

    compile_success, compile_msg = comp.compile_program()

    if compile_success:
        print_info(compile_msg)
    else:
        print_error(compile_msg)
        exit(1)

    print('开始渲染...')
    render_success, render_msg = comp.render_gif(gif_path)

    if render_success:
        print_info(render_msg)
    else:
        print_error(render_msg)
        exit(1)

    # 回切工作目录
    os.chdir(script_relative('.'))
    sys.path.remove(lang_path)

    encode_gif(args.force_dl, gif_path, mp4_path)
