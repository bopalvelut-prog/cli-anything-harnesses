from setuptools import setup
setup(
    name='cli-anything-zag',
    version='1.0.0',
    packages=['cli_anything.zag'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zag=cli_anything.zag:cli']},
)
