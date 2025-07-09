"""
function.py
Git/GitHub 规范化教学项目功能函数
"""
import requests


def greet(name: str):
    """打印问候信息，演示主功能结构"""
    print(f"Hello, {name}! 欢迎学习 Git/GitHub 规范化流程。")


# 调用 requests 获取 GitHub 状态
def fetch_github_status():
    """
    使用 requests 获取 GitHub 状态 API 示例
    返回 GitHub 状态信息（JSON）
    """
    url = "https://www.githubstatus.com/api/v2/status.json"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        print(f"GitHub 当前状态: {data['status']['description']}")
        return data
    except requests.RequestException as e:
        print(f"请求 GitHub 状态失败: {e}")
        return None
    # TODO: 针对可能的JSON解析错误，添加错误处理，commit类型: feat


# TODO: 一个有语法错误的函数，需要直接删除整个函数，并删除main中对该函数的调用，commit类型: fix
def lint_error():
    """
    一个有语法错误的函数，需要直接删除整个函数，并删除main中对该函数的调用
    """
    abc
    print('我是语法错误！')
