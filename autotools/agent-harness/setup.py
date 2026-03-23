from setuptools import setup
setup(
    name='cli-anything-autotools',
    version='1.0.0',
    packages=['cli_anything.autotools'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-autotools=cli_anything.autotools:cli']},
)
