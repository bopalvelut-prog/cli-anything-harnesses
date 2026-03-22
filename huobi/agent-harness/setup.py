from setuptools import setup
setup(
    name='cli-anything-huobi',
    version='1.0.0',
    packages=['cli_anything.huobi'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-huobi=cli_anything.huobi:cli']},
)
