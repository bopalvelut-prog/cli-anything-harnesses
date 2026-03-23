from setuptools import setup
setup(
    name='cli-anything-emergency',
    version='1.0.0',
    packages=['cli_anything.emergency'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-emergency=cli_anything.emergency:cli']},
)
