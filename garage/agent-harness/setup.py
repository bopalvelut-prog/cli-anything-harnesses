from setuptools import setup
setup(
    name='cli-anything-garage',
    version='1.0.0',
    packages=['cli_anything.garage'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-garage=cli_anything.garage:cli']},
)
