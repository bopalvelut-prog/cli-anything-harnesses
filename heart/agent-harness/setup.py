from setuptools import setup
setup(
    name='cli-anything-heart',
    version='1.0.0',
    packages=['cli_anything.heart'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-heart=cli_anything.heart:cli']},
)
