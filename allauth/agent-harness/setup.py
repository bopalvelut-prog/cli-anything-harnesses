from setuptools import setup
setup(
    name='cli-anything-allauth',
    version='1.0.0',
    packages=['cli_anything.allauth'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-allauth=cli_anything.allauth:cli']},
)
