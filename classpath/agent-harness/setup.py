from setuptools import setup
setup(
    name='cli-anything-classpath',
    version='1.0.0',
    packages=['cli_anything.classpath'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-classpath=cli_anything.classpath:cli']},
)
