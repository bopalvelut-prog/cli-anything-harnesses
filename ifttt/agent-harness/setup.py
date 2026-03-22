from setuptools import setup
setup(
    name='cli-anything-ifttt',
    version='1.0.0',
    packages=['cli_anything.ifttt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ifttt=cli_anything.ifttt:cli']},
)
