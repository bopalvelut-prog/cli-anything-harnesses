from setuptools import setup
setup(
    name='cli-anything-tensorboard',
    version='1.0.0',
    packages=['cli_anything.tensorboard'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tensorboard=cli_anything.tensorboard:cli']},
)
