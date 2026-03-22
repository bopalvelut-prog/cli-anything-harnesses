from setuptools import setup
setup(
    name='cli-anything-dashlane',
    version='1.0.0',
    packages=['cli_anything.dashlane'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dashlane=cli_anything.dashlane:cli']},
)
