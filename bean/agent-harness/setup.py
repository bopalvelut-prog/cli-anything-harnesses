from setuptools import setup
setup(
    name='cli-anything-bean',
    version='1.0.0',
    packages=['cli_anything.bean'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bean=cli_anything.bean:cli']},
)
