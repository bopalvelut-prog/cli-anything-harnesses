from setuptools import setup
setup(
    name='cli-anything-hls',
    version='1.0.0',
    packages=['cli_anything.hls'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hls=cli_anything.hls:cli']},
)
