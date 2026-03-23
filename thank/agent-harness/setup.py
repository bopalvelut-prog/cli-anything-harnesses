from setuptools import setup
setup(
    name='cli-anything-thank',
    version='1.0.0',
    packages=['cli_anything.thank'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-thank=cli_anything.thank:cli']},
)
