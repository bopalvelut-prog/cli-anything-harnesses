from setuptools import setup
setup(
    name='cli-anything-magit',
    version='1.0.0',
    packages=['cli_anything.magit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-magit=cli_anything.magit:cli']},
)
