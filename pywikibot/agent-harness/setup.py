from setuptools import setup
setup(
    name='cli-anything-pywikibot',
    version='1.0.0',
    packages=['cli_anything.pywikibot'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pywikibot=cli_anything.pywikibot:cli']},
)
