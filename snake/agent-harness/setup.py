from setuptools import setup
setup(
    name='cli-anything-snake',
    version='1.0.0',
    packages=['cli_anything.snake'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-snake=cli_anything.snake:cli']},
)
