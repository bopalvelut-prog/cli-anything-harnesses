from setuptools import setup
setup(
    name='cli-anything-close',
    version='1.0.0',
    packages=['cli_anything.close'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-close=cli_anything.close:cli']},
)
