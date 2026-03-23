from setuptools import setup
setup(
    name='cli-anything-spin',
    version='1.0.0',
    packages=['cli_anything.spin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-spin=cli_anything.spin:cli']},
)
