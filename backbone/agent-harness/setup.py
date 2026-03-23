from setuptools import setup
setup(
    name='cli-anything-backbone',
    version='1.0.0',
    packages=['cli_anything.backbone'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-backbone=cli_anything.backbone:cli']},
)
