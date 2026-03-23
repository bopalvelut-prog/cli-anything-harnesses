from setuptools import setup
setup(
    name='cli-anything-apex',
    version='1.0.0',
    packages=['cli_anything.apex'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apex=cli_anything.apex:cli']},
)
