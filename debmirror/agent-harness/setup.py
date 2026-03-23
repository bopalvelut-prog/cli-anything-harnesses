from setuptools import setup
setup(
    name='cli-anything-debmirror',
    version='1.0.0',
    packages=['cli_anything.debmirror'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-debmirror=cli_anything.debmirror:cli']},
)
