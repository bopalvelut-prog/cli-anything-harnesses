from setuptools import setup
setup(
    name='cli-anything-logseq',
    version='1.0.0',
    packages=['cli_anything.logseq'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-logseq=cli_anything.logseq:cli']},
)
