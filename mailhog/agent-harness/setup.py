from setuptools import setup
setup(
    name='cli-anything-mailhog',
    version='1.0.0',
    packages=['cli_anything.mailhog'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mailhog=cli_anything.mailhog:cli']},
)
