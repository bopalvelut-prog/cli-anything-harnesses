from setuptools import setup
setup(
    name='cli-anything-zip',
    version='1.0.0',
    packages=['cli_anything.zip'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zip=cli_anything.zip:cli']},
)
