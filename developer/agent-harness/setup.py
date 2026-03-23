from setuptools import setup
setup(
    name='cli-anything-developer',
    version='1.0.0',
    packages=['cli_anything.developer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-developer=cli_anything.developer:cli']},
)
