from setuptools import setup
setup(
    name='cli-anything-emphasis',
    version='1.0.0',
    packages=['cli_anything.emphasis'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-emphasis=cli_anything.emphasis:cli']},
)
