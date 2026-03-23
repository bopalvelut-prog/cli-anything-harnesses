from setuptools import setup
setup(
    name='cli-anything-pdfkit',
    version='1.0.0',
    packages=['cli_anything.pdfkit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pdfkit=cli_anything.pdfkit:cli']},
)
