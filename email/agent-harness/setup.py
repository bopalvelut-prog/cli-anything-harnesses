from setuptools import setup
setup(
    name='cli-anything-email',
    version='1.0.0',
    packages=['cli_anything.email'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-email=cli_anything.email:cli']},
)
