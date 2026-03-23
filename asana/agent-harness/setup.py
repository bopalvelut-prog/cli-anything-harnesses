from setuptools import setup
setup(
    name='cli-anything-asana',
    version='1.0.0',
    packages=['cli_anything.asana'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-asana=cli_anything.asana:cli']},
)
