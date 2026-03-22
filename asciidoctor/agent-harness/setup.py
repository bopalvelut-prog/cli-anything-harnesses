from setuptools import setup
setup(
    name='cli-anything-asciidoctor',
    version='1.0.0',
    packages=['cli_anything.asciidoctor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-asciidoctor=cli_anything.asciidoctor:cli']},
)
