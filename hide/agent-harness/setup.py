from setuptools import setup
setup(
    name='cli-anything-hide',
    version='1.0.0',
    packages=['cli_anything.hide'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hide=cli_anything.hide:cli']},
)
