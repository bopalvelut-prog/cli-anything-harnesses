from setuptools import setup
setup(
    name='cli-anything-moral',
    version='1.0.0',
    packages=['cli_anything.moral'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-moral=cli_anything.moral:cli']},
)
