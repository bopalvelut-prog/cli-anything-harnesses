from setuptools import setup
setup(
    name='cli-anything-php',
    version='1.0.0',
    packages=['cli_anything.php'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-php=cli_anything.php:cli']},
)
