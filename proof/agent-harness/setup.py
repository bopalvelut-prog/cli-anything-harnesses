from setuptools import setup
setup(
    name='cli-anything-proof',
    version='1.0.0',
    packages=['cli_anything.proof'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-proof=cli_anything.proof:cli']},
)
