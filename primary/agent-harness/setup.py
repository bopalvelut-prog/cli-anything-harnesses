from setuptools import setup
setup(
    name='cli-anything-primary',
    version='1.0.0',
    packages=['cli_anything.primary'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-primary=cli_anything.primary:cli']},
)
