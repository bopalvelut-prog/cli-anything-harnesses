from setuptools import setup
setup(
    name='cli-anything-autorest',
    version='1.0.0',
    packages=['cli_anything.autorest'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-autorest=cli_anything.autorest:cli']},
)
