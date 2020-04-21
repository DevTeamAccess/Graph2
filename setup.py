from setuptools import setup
# with open('README.md') as f:
#     long_description = f.read()
setup(
    name="GraphQLTest",
    description="Add .env support to your  development and deployments",
    zip_safe=False,
    entry_points='''
        [console_scripts]
        Run=RunApp.cli:cli
    ''',
)