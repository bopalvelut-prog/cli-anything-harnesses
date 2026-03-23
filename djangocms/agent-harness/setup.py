from setuptools import setup
setup(
    name='cli-anything-djangocms',
    version='1.0.0',
    packages=['cli_anything.djangocms'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-djangocms=cli_anything.djangocms:cli']},
)
