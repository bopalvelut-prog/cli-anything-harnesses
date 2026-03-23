from setuptools import setup
setup(
    name='cli-anything-pixmap',
    version='1.0.0',
    packages=['cli_anything.pixmap'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pixmap=cli_anything.pixmap:cli']},
)
