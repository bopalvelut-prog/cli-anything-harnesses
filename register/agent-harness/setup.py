from setuptools import setup
setup(
    name='cli-anything-register',
    version='1.0.0',
    packages=['cli_anything.register'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-register=cli_anything.register:cli']},
)
