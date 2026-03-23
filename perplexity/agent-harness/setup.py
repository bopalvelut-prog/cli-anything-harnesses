from setuptools import setup
setup(
    name='cli-anything-perplexity',
    version='1.0.0',
    packages=['cli_anything.perplexity'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-perplexity=cli_anything.perplexity:cli']},
)
