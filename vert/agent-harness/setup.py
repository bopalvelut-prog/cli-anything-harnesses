from setuptools import setup
setup(
    name='cli-anything-vert',
    version='1.0.0',
    packages=['cli_anything.vert'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vert=cli_anything.vert:cli']},
)
