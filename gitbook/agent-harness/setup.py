from setuptools import setup
setup(
    name='cli-anything-gitbook',
    version='1.0.0',
    packages=['cli_anything.gitbook'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gitbook=cli_anything.gitbook:cli']},
)
