from setuptools import setup
setup(
    name='cli-anything-pollution',
    version='1.0.0',
    packages=['cli_anything.pollution'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pollution=cli_anything.pollution:cli']},
)
