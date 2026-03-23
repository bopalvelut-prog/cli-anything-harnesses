from setuptools import setup
setup(
    name='cli-anything-cancel',
    version='1.0.0',
    packages=['cli_anything.cancel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cancel=cli_anything.cancel:cli']},
)
