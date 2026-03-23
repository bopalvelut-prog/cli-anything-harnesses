from setuptools import setup
setup(
    name='cli-anything-spiritual',
    version='1.0.0',
    packages=['cli_anything.spiritual'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-spiritual=cli_anything.spiritual:cli']},
)
