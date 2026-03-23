from setuptools import setup
setup(
    name='cli-anything-current',
    version='1.0.0',
    packages=['cli_anything.current'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-current=cli_anything.current:cli']},
)
