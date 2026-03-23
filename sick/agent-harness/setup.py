from setuptools import setup
setup(
    name='cli-anything-sick',
    version='1.0.0',
    packages=['cli_anything.sick'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sick=cli_anything.sick:cli']},
)
