from setuptools import setup
setup(
    name='cli-anything-fsck',
    version='1.0.0',
    packages=['cli_anything.fsck'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fsck=cli_anything.fsck:cli']},
)
