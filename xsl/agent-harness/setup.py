from setuptools import setup
setup(
    name='cli-anything-xsl',
    version='1.0.0',
    packages=['cli_anything.xsl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xsl=cli_anything.xsl:cli']},
)
