from setuptools import setup
setup(
    name='cli-anything-production',
    version='1.0.0',
    packages=['cli_anything.production'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-production=cli_anything.production:cli']},
)
