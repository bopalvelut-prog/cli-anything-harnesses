from setuptools import setup
setup(
    name='cli-anything-use',
    version='1.0.0',
    packages=['cli_anything.use'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-use=cli_anything.use:cli']},
)
