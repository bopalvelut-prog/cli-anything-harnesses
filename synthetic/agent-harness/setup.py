from setuptools import setup
setup(
    name='cli-anything-synthetic',
    version='1.0.0',
    packages=['cli_anything.synthetic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-synthetic=cli_anything.synthetic:cli']},
)
