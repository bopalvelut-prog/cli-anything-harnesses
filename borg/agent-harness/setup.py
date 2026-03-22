from setuptools import setup
setup(
    name='cli-anything-borg',
    version='1.0.0',
    packages=['cli_anything.borg'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-borg=cli_anything.borg:cli']},
)
