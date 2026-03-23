from setuptools import setup
setup(
    name='cli-anything-upload',
    version='1.0.0',
    packages=['cli_anything.upload'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-upload=cli_anything.upload:cli']},
)
