from setuptools import setup
setup(
    name='cli-anything-zero_mq',
    version='1.0.0',
    packages=['cli_anything.zero_mq'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zero_mq=cli_anything.zero_mq:cli']},
)
