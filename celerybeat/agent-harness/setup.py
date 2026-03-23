from setuptools import setup
setup(
    name='cli-anything-celerybeat',
    version='1.0.0',
    packages=['cli_anything.celerybeat'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-celerybeat=cli_anything.celerybeat:cli']},
)
