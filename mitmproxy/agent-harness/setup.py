from setuptools import setup
setup(
    name='cli-anything-mitmproxy',
    version='1.0.0',
    packages=['cli_anything.mitmproxy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mitmproxy=cli_anything.mitmproxy:cli']},
)
