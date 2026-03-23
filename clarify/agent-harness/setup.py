from setuptools import setup
setup(
    name='cli-anything-clarify',
    version='1.0.0',
    packages=['cli_anything.clarify'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-clarify=cli_anything.clarify:cli']},
)
