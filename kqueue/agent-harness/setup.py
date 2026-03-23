from setuptools import setup
setup(
    name='cli-anything-kqueue',
    version='1.0.0',
    packages=['cli_anything.kqueue'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kqueue=cli_anything.kqueue:cli']},
)
