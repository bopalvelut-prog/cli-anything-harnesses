from setuptools import setup
setup(
    name='cli-anything-prayer',
    version='1.0.0',
    packages=['cli_anything.prayer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prayer=cli_anything.prayer:cli']},
)
