from setuptools import setup
setup(
    name='cli-anything-plausible',
    version='1.0.0',
    packages=['cli_anything.plausible'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-plausible=cli_anything.plausible:cli']},
)
