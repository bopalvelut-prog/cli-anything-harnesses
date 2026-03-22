from setuptools import setup
setup(
    name='cli-anything-makemkv',
    version='1.0.0',
    packages=['cli_anything.makemkv'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-makemkv=cli_anything.makemkv:cli']},
)
