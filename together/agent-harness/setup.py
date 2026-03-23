from setuptools import setup
setup(
    name='cli-anything-together',
    version='1.0.0',
    packages=['cli_anything.together'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-together=cli_anything.together:cli']},
)
