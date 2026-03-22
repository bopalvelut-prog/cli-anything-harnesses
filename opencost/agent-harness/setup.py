from setuptools import setup
setup(
    name='cli-anything-opencost',
    version='1.0.0',
    packages=['cli_anything.opencost'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-opencost=cli_anything.opencost:cli']},
)
