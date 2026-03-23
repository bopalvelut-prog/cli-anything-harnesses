from setuptools import setup
setup(
    name='cli-anything-port',
    version='1.0.0',
    packages=['cli_anything.port'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-port=cli_anything.port:cli']},
)
