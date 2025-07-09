"""
main.py
Git/GitHub 规范化教学项目主程序
"""

import argparse
from function import greet, fetch_github_status, lint_error


def main():
    """主函数，解析命令行参数并调用核心功能"""
    parser = argparse.ArgumentParser(
        description="Git/GitHub 规范化教学项目示例主程序"
    )
    parser.add_argument(
        "--name", "-n", default="github-flow 学员", help="你的名字（可选）"
    )
    parser.add_argument(
        "--check-status", "-c", action="store_true", help="演示调用 requests 获取 GitHub 状态"
    )
    parser.add_argument(
        "--lint-error", "-l", action="store_true", help="演示修复语法错误"
    )
    args = parser.parse_args()
    greet(args.name)
    if args.check_status:
        fetch_github_status()
    if args.lint_error:
        lint_error()


if __name__ == "__main__":
    main()
