from setuptools import setup
setup(
    name='cli-anything-patch',
    version='1.0.0',
    packages=['cli_anything.patch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-patch=cli_anything.patch:cli']},
)
