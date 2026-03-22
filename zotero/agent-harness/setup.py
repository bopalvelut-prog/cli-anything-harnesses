from setuptools import setup
setup(
    name='cli-anything-zotero',
    version='1.0.0',
    packages=['cli_anything.zotero'],
    install_requires=['click', 'requests'],
    entry_points={'console_scripts': ['cli-anything-zotero=cli_anything.zotero:cli']},
)
