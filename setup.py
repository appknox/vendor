from setuptools import setup, find_packages

__VERSION__ = '0.9.93'

setup(
    name='ak-vendor',
    version=__VERSION__,
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
        'Programming Language :: Python :: 3.6',
    ],

    keywords='appknox vendor',
    packages=find_packages(),
    data_files=[
        ('excel', ['ak_vendor/translations/ja/vulnerability.xlsx']),
        ('report', [
            'ak_vendor/report.html',
            'ak_vendor/report.css',
            'ak_vendor/report/report_template.html',
        ]),
        ('translations', ['ak_vendor/locale/ja/LC_MESSAGES/django.po']),
    ],
    include_package_data=True,
    entry_points='',
    install_requires=[
        'orm-choices==0.3.0',
        'maya==0.5.0',
        'html2text==2018.1.9',
    ],
    zip_safe=False,
    extras_require={
        'dev': [
            'django==2.0.2',
            'weasyprint==0.42.2',
            'bumpversion==0.5.3',
            'twine==1.9.1'
        ],
        'test': [''],
    },
)
