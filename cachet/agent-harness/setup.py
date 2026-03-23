from setuptools import setup
setup(
    name='cli-anything-cachet',
    version='1.0.0',
    packages=['cli_anything.cachet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cachet=cli_anything.cachet:cli']},
)
