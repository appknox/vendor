from setuptools import setup, find_packages

setup(
    name='ak-vendor',
    version='0.9.23',
    description="Some vendor scripts that we use here at Appknox",
    long_description="All the Vendor/helper files the Appknox relies on",
    url='https://github.com/appknox/vendor',
    author='dhilipsiva',
    author_email='dhilipsiva@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='appknox vendor',
    packages=find_packages(),
    data_files=[
        ('excel', ['ak_vendor/translations/ja/subheading.xlsx',
                   'ak_vendor/translations/ja/vulnerability.xlsx']),
        ('report', ['ak_vendor/report.html']),
    ],
    include_package_data=True,
    entry_points='',
    install_requires=[
        "python3-protobuf==2.5.0",
    ],
    zip_safe=False,
    extras_require={
        'dev': [''],
        'test': [''],
    },
)
