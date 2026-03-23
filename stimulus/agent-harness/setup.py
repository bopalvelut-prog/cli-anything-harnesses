from setuptools import setup
setup(
    name='cli-anything-stimulus',
    version='1.0.0',
    packages=['cli_anything.stimulus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stimulus=cli_anything.stimulus:cli']},
)
