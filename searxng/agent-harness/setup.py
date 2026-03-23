from setuptools import setup
setup(
    name='cli-anything-searxng',
    version='1.0.0',
    packages=['cli_anything.searxng'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-searxng=cli_anything.searxng:cli']},
)
