from setuptools import setup
setup(
    name='cli-anything-processmaker',
    version='1.0.0',
    packages=['cli_anything.processmaker'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-processmaker=cli_anything.processmaker:cli']},
)
