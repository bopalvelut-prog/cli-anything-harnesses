from setuptools import setup
setup(
    name='cli-anything-gorm',
    version='1.0.0',
    packages=['cli_anything.gorm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gorm=cli_anything.gorm:cli']},
)
