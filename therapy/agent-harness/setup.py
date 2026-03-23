from setuptools import setup
setup(
    name='cli-anything-therapy',
    version='1.0.0',
    packages=['cli_anything.therapy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-therapy=cli_anything.therapy:cli']},
)
