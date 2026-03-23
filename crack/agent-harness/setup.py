from setuptools import setup
setup(
    name='cli-anything-crack',
    version='1.0.0',
    packages=['cli_anything.crack'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-crack=cli_anything.crack:cli']},
)
