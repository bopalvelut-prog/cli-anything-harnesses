from setuptools import setup
setup(
    name='cli-anything-hello',
    version='1.0.0',
    packages=['cli_anything.hello'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hello=cli_anything.hello:cli']},
)
