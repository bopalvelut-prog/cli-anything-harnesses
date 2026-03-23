from setuptools import setup
setup(
    name='cli-anything-utf',
    version='1.0.0',
    packages=['cli_anything.utf'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-utf=cli_anything.utf:cli']},
)
