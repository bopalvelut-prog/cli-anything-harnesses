from setuptools import setup
setup(
    name='cli-anything-btrfs',
    version='1.0.0',
    packages=['cli_anything.btrfs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-btrfs=cli_anything.btrfs:cli']},
)
