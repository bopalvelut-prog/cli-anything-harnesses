from setuptools import setup
setup(
    name='cli-anything-aurora_mysql',
    version='1.0.0',
    packages=['cli_anything.aurora_mysql'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aurora_mysql=cli_anything.aurora_mysql:cli']},
)
