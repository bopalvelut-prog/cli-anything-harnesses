from setuptools import setup
setup(
    name='cli-anything-graphana',
    version='1.0.0',
    packages=['cli_anything.graphana'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-graphana=cli_anything.graphana:cli']},
)
