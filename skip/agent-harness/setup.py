from setuptools import setup
setup(
    name='cli-anything-skip',
    version='1.0.0',
    packages=['cli_anything.skip'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-skip=cli_anything.skip:cli']},
)
