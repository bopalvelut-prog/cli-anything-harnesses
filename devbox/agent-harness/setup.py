from setuptools import setup
setup(
    name='cli-anything-devbox',
    version='1.0.0',
    packages=['cli_anything.devbox'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-devbox=cli_anything.devbox:cli']},
)
