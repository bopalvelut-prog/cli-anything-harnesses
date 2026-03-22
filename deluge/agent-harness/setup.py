from setuptools import setup
setup(
    name='cli-anything-deluge',
    version='1.0.0',
    packages=['cli_anything.deluge'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-deluge=cli_anything.deluge:cli']},
)
