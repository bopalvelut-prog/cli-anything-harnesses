from setuptools import setup
setup(
    name='cli-anything-somewhere',
    version='1.0.0',
    packages=['cli_anything.somewhere'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-somewhere=cli_anything.somewhere:cli']},
)
