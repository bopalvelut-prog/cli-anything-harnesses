from setuptools import setup
setup(
    name='cli-anything-training',
    version='1.0.0',
    packages=['cli_anything.training'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-training=cli_anything.training:cli']},
)
