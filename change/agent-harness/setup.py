from setuptools import setup
setup(
    name='cli-anything-change',
    version='1.0.0',
    packages=['cli_anything.change'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-change=cli_anything.change:cli']},
)
