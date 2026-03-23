from setuptools import setup
setup(
    name='cli-anything-mxnet',
    version='1.0.0',
    packages=['cli_anything.mxnet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mxnet=cli_anything.mxnet:cli']},
)
