from setuptools import setup
setup(
    name='cli-anything-cubefs',
    version='1.0.0',
    packages=['cli_anything.cubefs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cubefs=cli_anything.cubefs:cli']},
)
