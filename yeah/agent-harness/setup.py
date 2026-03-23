from setuptools import setup
setup(
    name='cli-anything-yeah',
    version='1.0.0',
    packages=['cli_anything.yeah'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-yeah=cli_anything.yeah:cli']},
)
