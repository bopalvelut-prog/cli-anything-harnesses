from setuptools import setup
setup(
    name='cli-anything-device',
    version='1.0.0',
    packages=['cli_anything.device'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-device=cli_anything.device:cli']},
)
