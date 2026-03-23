from setuptools import setup
setup(
    name='cli-anything-udev',
    version='1.0.0',
    packages=['cli_anything.udev'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-udev=cli_anything.udev:cli']},
)
