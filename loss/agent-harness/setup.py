from setuptools import setup
setup(
    name='cli-anything-loss',
    version='1.0.0',
    packages=['cli_anything.loss'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-loss=cli_anything.loss:cli']},
)
