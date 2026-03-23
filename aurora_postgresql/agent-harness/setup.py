from setuptools import setup
setup(
    name='cli-anything-aurora_postgresql',
    version='1.0.0',
    packages=['cli_anything.aurora_postgresql'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aurora_postgresql=cli_anything.aurora_postgresql:cli']},
)
