from setuptools import setup
setup(
    name='cli-anything-creative',
    version='1.0.0',
    packages=['cli_anything.creative'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-creative=cli_anything.creative:cli']},
)
