from setuptools import setup
setup(
    name='cli-anything-mp4',
    version='1.0.0',
    packages=['cli_anything.mp4'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mp4=cli_anything.mp4:cli']},
)
