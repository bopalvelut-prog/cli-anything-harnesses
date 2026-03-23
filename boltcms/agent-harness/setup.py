from setuptools import setup
setup(
    name='cli-anything-boltcms',
    version='1.0.0',
    packages=['cli_anything.boltcms'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-boltcms=cli_anything.boltcms:cli']},
)
