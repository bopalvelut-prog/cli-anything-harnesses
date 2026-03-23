from setuptools import setup
setup(
    name='cli-anything-warm',
    version='1.0.0',
    packages=['cli_anything.warm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-warm=cli_anything.warm:cli']},
)
