from setuptools import setup
setup(
    name='cli-anything-present',
    version='1.0.0',
    packages=['cli_anything.present'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-present=cli_anything.present:cli']},
)
