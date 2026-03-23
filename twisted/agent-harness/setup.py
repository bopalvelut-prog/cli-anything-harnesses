from setuptools import setup
setup(
    name='cli-anything-twisted',
    version='1.0.0',
    packages=['cli_anything.twisted'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-twisted=cli_anything.twisted:cli']},
)
