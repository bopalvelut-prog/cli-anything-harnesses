from setuptools import setup
setup(
    name='cli-anything-illumos',
    version='1.0.0',
    packages=['cli_anything.illumos'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-illumos=cli_anything.illumos:cli']},
)
