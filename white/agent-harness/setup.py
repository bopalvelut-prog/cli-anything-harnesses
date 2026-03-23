from setuptools import setup
setup(
    name='cli-anything-white',
    version='1.0.0',
    packages=['cli_anything.white'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-white=cli_anything.white:cli']},
)
