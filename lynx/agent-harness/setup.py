from setuptools import setup
setup(
    name='cli-anything-lynx',
    version='1.0.0',
    packages=['cli_anything.lynx'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lynx=cli_anything.lynx:cli']},
)
