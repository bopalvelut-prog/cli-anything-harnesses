from setuptools import setup
setup(
    name='cli-anything-keepassxc',
    version='1.0.0',
    packages=['cli_anything.keepassxc'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-keepassxc=cli_anything.keepassxc:cli']},
)
