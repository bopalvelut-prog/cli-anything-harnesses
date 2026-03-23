from setuptools import setup
setup(
    name='cli-anything-tinker',
    version='1.0.0',
    packages=['cli_anything.tinker'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tinker=cli_anything.tinker:cli']},
)
