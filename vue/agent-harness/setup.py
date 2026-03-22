from setuptools import setup
setup(
    name='cli-anything-vue',
    version='1.0.0',
    packages=['cli_anything.vue'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vue=cli_anything.vue:cli']},
)
