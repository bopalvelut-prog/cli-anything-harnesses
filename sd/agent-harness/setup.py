from setuptools import setup
setup(
    name='cli-anything-sd',
    version='1.0.0',
    packages=['cli_anything.sd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sd=cli_anything.sd:cli']},
)
