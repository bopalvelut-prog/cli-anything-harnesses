from setuptools import setup
setup(
    name='cli-anything-cuda',
    version='1.0.0',
    packages=['cli_anything.cuda'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cuda=cli_anything.cuda:cli']},
)
