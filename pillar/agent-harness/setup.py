from setuptools import setup
setup(
    name='cli-anything-pillar',
    version='1.0.0',
    packages=['cli_anything.pillar'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pillar=cli_anything.pillar:cli']},
)
