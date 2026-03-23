from setuptools import setup
setup(
    name='cli-anything-adobe',
    version='1.0.0',
    packages=['cli_anything.adobe'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-adobe=cli_anything.adobe:cli']},
)
