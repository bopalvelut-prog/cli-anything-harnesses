from setuptools import setup
setup(
    name='cli-anything-easy',
    version='1.0.0',
    packages=['cli_anything.easy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-easy=cli_anything.easy:cli']},
)
