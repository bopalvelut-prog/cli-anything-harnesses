from setuptools import setup
setup(
    name='cli-anything-useful',
    version='1.0.0',
    packages=['cli_anything.useful'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-useful=cli_anything.useful:cli']},
)
