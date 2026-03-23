from setuptools import setup
setup(
    name='cli-anything-rke',
    version='1.0.0',
    packages=['cli_anything.rke'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rke=cli_anything.rke:cli']},
)
