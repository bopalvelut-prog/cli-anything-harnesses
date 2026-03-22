from setuptools import setup
setup(
    name='cli-anything-tmux',
    version='1.0.0',
    packages=['cli_anything.tmux'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tmux=cli_anything.tmux:cli']},
)
