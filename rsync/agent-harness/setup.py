from setuptools import setup
setup(
    name='cli-anything-rsync',
    version='1.0.0',
    packages=['cli_anything.rsync'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rsync=cli_anything.rsync:cli']},
)
