from setuptools import setup
setup(
    name='cli-anything-carbon',
    version='1.0.0',
    packages=['cli_anything.carbon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-carbon=cli_anything.carbon:cli']},
)
