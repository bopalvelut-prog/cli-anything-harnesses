from setuptools import setup
setup(
    name='cli-anything-sentinel',
    version='1.0.0',
    packages=['cli_anything.sentinel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sentinel=cli_anything.sentinel:cli']},
)
