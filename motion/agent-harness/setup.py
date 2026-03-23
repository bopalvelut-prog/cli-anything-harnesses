from setuptools import setup
setup(
    name='cli-anything-motion',
    version='1.0.0',
    packages=['cli_anything.motion'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-motion=cli_anything.motion:cli']},
)
