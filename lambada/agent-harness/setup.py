from setuptools import setup
setup(
    name='cli-anything-lambada',
    version='1.0.0',
    packages=['cli_anything.lambada'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lambada=cli_anything.lambada:cli']},
)
