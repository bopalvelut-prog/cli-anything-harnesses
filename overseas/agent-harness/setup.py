from setuptools import setup
setup(
    name='cli-anything-overseas',
    version='1.0.0',
    packages=['cli_anything.overseas'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-overseas=cli_anything.overseas:cli']},
)
