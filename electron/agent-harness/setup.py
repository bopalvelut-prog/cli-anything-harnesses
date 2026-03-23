from setuptools import setup
setup(
    name='cli-anything-electron',
    version='1.0.0',
    packages=['cli_anything.electron'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-electron=cli_anything.electron:cli']},
)
