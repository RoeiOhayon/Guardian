from distutils.core import setup

setup(
    name='guardian-python',
    packages=['guardian', 'guardian.atomic_guards'],
    version='1.1.1',
    description='Guard Clause Package',
    long_description="Guardian allows you to use guard clauses both as function decorators and regular guard clauses\n"
                     "Guard Clause Decorators allow you to check all of a function's arguments.\n"
                     "Guardian also enable you to create your own custom guard clauses.\n\nLatest Version: 1.1.1\n"
                     "Come visit: https://github.com/RoeiOhayon/Guardian",
    author='Roei Ohayon',
    maintainer='Roei Ohayon',
    author_email='roeiohayon1652@gmail.com',
    url='https://github.com/RoeiOhayon/Guardian',
    project_urls={"GitHub": "https://github.com/RoeiOhayon/Guardian"}
)
