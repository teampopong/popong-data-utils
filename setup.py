from setuptools import setup

setup(
    name='popong_data_utils',
    version='0.1.2-dev',
    url='http://github.com/teampopong/popong-data-utils/',
    license='BSD',
    author='Cheol Kang',
    author_email='steel@popong.com',
    description='A Korean political data models made by '
                'team POPONG',
    packages=['popong_data_utils'],
    platforms='any',
    include_package_data=True,
    install_requires=[
        'SQLAlchemy>=0.8.1',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
