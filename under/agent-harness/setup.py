from setuptools import setup
setup(
    name='cli-anything-under',
    version='1.0.0',
    packages=['cli_anything.under'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-under=cli_anything.under:cli']},
)
