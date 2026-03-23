from setuptools import setup
setup(
    name='cli-anything-staff',
    version='1.0.0',
    packages=['cli_anything.staff'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-staff=cli_anything.staff:cli']},
)
