from setuptools import setup
setup(
    name='cli-anything-nose',
    version='1.0.0',
    packages=['cli_anything.nose'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nose=cli_anything.nose:cli']},
)
