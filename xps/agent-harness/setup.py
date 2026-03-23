from setuptools import setup
setup(
    name='cli-anything-xps',
    version='1.0.0',
    packages=['cli_anything.xps'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xps=cli_anything.xps:cli']},
)
