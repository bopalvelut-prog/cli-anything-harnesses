from setuptools import setup
setup(
    name='cli-anything-swap',
    version='1.0.0',
    packages=['cli_anything.swap'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-swap=cli_anything.swap:cli']},
)
