from setuptools import setup
setup(
    name='cli-anything-scalyr',
    version='1.0.0',
    packages=['cli_anything.scalyr'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scalyr=cli_anything.scalyr:cli']},
)
