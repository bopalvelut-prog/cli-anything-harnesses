from setuptools import setup
setup(
    name='cli-anything-freshrss',
    version='1.0.0',
    packages=['cli_anything.freshrss'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-freshrss=cli_anything.freshrss:cli']},
)
