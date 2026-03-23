from setuptools import setup
setup(
    name='cli-anything-send',
    version='1.0.0',
    packages=['cli_anything.send'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-send=cli_anything.send:cli']},
)
