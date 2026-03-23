from setuptools import setup
setup(
    name='cli-anything-particular',
    version='1.0.0',
    packages=['cli_anything.particular'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-particular=cli_anything.particular:cli']},
)
