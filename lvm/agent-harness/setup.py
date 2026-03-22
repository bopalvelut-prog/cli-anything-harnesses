from setuptools import setup
setup(
    name='cli-anything-lvm',
    version='1.0.0',
    packages=['cli_anything.lvm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lvm=cli_anything.lvm:cli']},
)
