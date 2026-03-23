from setuptools import setup
setup(
    name='cli-anything-torch',
    version='1.0.0',
    packages=['cli_anything.torch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-torch=cli_anything.torch:cli']},
)
