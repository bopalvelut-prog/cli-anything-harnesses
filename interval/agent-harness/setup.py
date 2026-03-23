from setuptools import setup
setup(
    name='cli-anything-interval',
    version='1.0.0',
    packages=['cli_anything.interval'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-interval=cli_anything.interval:cli']},
)
