from setuptools import setup
setup(
    name='cli-anything-hipchat',
    version='1.0.0',
    packages=['cli_anything.hipchat'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hipchat=cli_anything.hipchat:cli']},
)
