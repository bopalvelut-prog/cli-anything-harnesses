from setuptools import setup
setup(
    name='cli-anything-fzf',
    version='1.0.0',
    packages=['cli_anything.fzf'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fzf=cli_anything.fzf:cli']},
)
