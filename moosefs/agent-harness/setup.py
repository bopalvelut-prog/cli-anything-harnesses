from setuptools import setup
setup(
    name='cli-anything-moosefs',
    version='1.0.0',
    packages=['cli_anything.moosefs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-moosefs=cli_anything.moosefs:cli']},
)
