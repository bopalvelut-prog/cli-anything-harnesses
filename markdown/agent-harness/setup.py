from setuptools import setup
setup(
    name='cli-anything-markdown',
    version='1.0.0',
    packages=['cli_anything.markdown'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-markdown=cli_anything.markdown:cli']},
)
