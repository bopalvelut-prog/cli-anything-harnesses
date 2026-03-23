from setuptools import setup
setup(
    name='cli-anything-ball',
    version='1.0.0',
    packages=['cli_anything.ball'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ball=cli_anything.ball:cli']},
)
