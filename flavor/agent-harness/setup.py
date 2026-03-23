from setuptools import setup
setup(
    name='cli-anything-flavor',
    version='1.0.0',
    packages=['cli_anything.flavor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-flavor=cli_anything.flavor:cli']},
)
