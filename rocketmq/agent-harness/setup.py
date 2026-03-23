from setuptools import setup
setup(
    name='cli-anything-rocketmq',
    version='1.0.0',
    packages=['cli_anything.rocketmq'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rocketmq=cli_anything.rocketmq:cli']},
)
