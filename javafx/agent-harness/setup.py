from setuptools import setup
setup(
    name='cli-anything-javafx',
    version='1.0.0',
    packages=['cli_anything.javafx'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-javafx=cli_anything.javafx:cli']},
)
