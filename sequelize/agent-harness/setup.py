from setuptools import setup
setup(
    name='cli-anything-sequelize',
    version='1.0.0',
    packages=['cli_anything.sequelize'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sequelize=cli_anything.sequelize:cli']},
)
