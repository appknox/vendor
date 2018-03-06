#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#
# flake8: noqa

"""
File name: seed.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2017-03-30
"""
from copy import copy
from ak_vendor import owasp
from ak_vendor.utils import dict2obj
OWASP_DATA = {d['id']: dict2obj(d) for d in owasp.data}


vulnerability_template = {
    'business_implication': '<p>With Cordova 3.5.0 or prior, attackers may:</p><p>Para2 With Cordova 3.5.0 or prior, attackers may:</p><ul><li>Open and send data to arbitrary applications.</li><li>Bypass the HTTP whitelist and connect to arbitrary servers.</li><li>Change the start page via a crafted intent URL.</li></ul>',
    'compliant': '<p>Ensure that the <code>android:debuggable</code> attribute is set to false before the app is released:</p>\n<pre><code>android:debuggable=&quot;false&quot;</code></pre>\n<p>Note that some development environments (including Eclipse/ADT and Ant) automatically set <code>android:debuggable</code> to true for incremental or debugging builds but set it to false for release builds.</p>\n',
    'description': '<p>Debugging was enabled on the app which makes it easier for reverseengineers to hook a debugger to it. This allows dumping a stack traceand accessing debugging helper classes.</p>',
    'heading': 'Do not release apps that are debuggable',
    'intro': '<p>Android allows the attribute <code>android:debuggable</code> to be set to true so that the app can be debugged. By default this attribute is disabled, i.e., it is set to false, but it may be set to true to help with debugging during development of the app. However, an app should never be released with this attribute set to true as it enables users to gain access to details of the app that should be kept secure. With the attribute set to true, users can debug the app even without access to its source code.</p>\n',
    'name': 'Application Debug Enabled',
    'non_compliant': '<p>This non-compliant code example shows an app that has the <code>android:debuggable</code> attribute set to true being accessed to reveal sensitive data.</p>\n<pre><code>$ adb shell\nshell@android:/ $ run-as com.example.someapp sh\nshell@android:/data/data/com.example.someapp $ id\nuid=10060(app_60) gid=10060(app_60)\nshell@android:/data/data/com.example.someapp $ ls files/\nsecret_data.txt\nshell@android:/data/data/com.example.some $ cat files/secret_data.txt\npassword=GoogolPlex\naccount_number=31974286</code></pre>\n<p>Clearly, with the <code>android:debuggable</code> attribute set to true, sensitive date related to the app can be revealed to any user.</p>\n',
    'question': 'Does the application has Debug enabled?',
    'related_to': '<p>With Cordova 3.5.0 or prior, attackers may:</p><p>Para2 With Cordova 3.5.0 or prior, attackers may:</p><ul><li>Open and send data to arbitrary applications.</li><li>Bypass the HTTP whitelist and connect to arbitrary servers.</li><li>Change the start page via a crafted intent URL.</li></ul>',
    'success_message': 'Debugging was disabled',
    'types': ["Static","Dynamic","API","Manual"],
    'uuid': '84b86ac9-a60e-40ef-ab1b-fc8ec39f6e1d',
    'id': 3
}



analysis_template = {
    'analiser_version': 0,
    'created_on': '2017-03-03 09:17:31.849832+00:00',
    'findings': [
        {'title': None, 'description': 'This application opens a socket and connects to it, which might be insecured, defined at Lcom/e/a/a/a/q;->b'},
        {'title': None, 'description': 'This application opens a socket and connects to it, which might be insecured, defined at Lcom/e/a/a/a/p;->a'},
        {'title': None, 'description': 'This application opens a socket and connects to it, which might be insecured, defined at Lcom/e/a/a/a/p;->d'},
        {'title': None, 'description': 'This application opens a socket and connects to it, which might be insecured, defined at Lcom/e/a/a/a/p;->f'},
        {'title': "Debug was enabled on the app which make it easier for attackers to hook a debugger, dump a stack trace and access debugging helper classes.", "description": "<application android:debuggable='true' Debug enabled for app"},
    ],
    'risk': 1,
    'status': 1,
    'updated_on': '2017-03-03 09:18:14.704847+00:00',
    'uuid': '9d522cf6-ce5c-4bef-9d96-2e641c2e65be',
    'id': 135,
    'vulnerability': vulnerability_template,
    'color': 'red',
    'get_risk_display': 'High',
    'show_cvss': True,
    'cvss_base': 6.7,
    'cvss_version': 3,
    'cvss_metrics_humanized': [
        {'key': 'Integrity Impact', 'value': 'Low'},
        {'key': 'Attack Vector', 'value': 'Network'},
        {'key': 'Availability Impact', 'value': 'None'},
        {'key': 'Confidentiality Impact', 'value': 'Low'},
        {'key': 'Attack Complexity', 'value': 'Low'},
        {'key': 'User Interaction', 'value': 'Not Required'},
        {'key': 'Privileges Required', 'value': 'High'}
        ],
        'owasp': ['M1_2016', 'M10_2016', 'A1_2013'],
        'owasp_categories': [
            OWASP_DATA.get('M1_2016'), OWASP_DATA.get('M10_2016'),
            OWASP_DATA.get('A1_2013')
        ]
 }

analiser1 = copy(analysis_template)
analiser2 = copy(analysis_template)
vulnerability1 = copy(vulnerability_template)
vulnerability2 = copy(vulnerability_template)

vulnerability2['related_to'] = '<ul> <li>Facebook SDK for Android: <a href="http://readwrite.com/2012/04/10/what-developers-and-users-can#awesm=~o9iqZAMlUPshPu" class="uri">http://readwrite.com/2012/04/10/what-developers-and-users-can#awesm=~o9iqZAMlUPshPu</a></li> <li><a href="https://jvn.jp/en/jp/JVN23328321/">JVN#23328321</a> Puella Magi Madoka Magica iP for Android vulnerable to information disclosure</li> <li><a href="https://jvn.jp/en/jp/JVN86040029/">JVN#86040029</a> Weathernews Touch for Android stores location information in the system log file</li> <li><a href="https://jvn.jp/en/jp/JVN33159152/">JVN#33159152</a> Loctouch for Android information management vulnerability</li> <li><a href="https://jvn.jp/en/jp/JVN56923652/">JVN#56923652</a> Monaca Debugger for Android information management vulnerability</li> </ul>'
vulnerability2['non_compliant'] = '<ol style="list-style-type: decimal"> <li>Facebook SDK for Android contained the following code which sends Facebook access tokens to log output in plain text format.</p> <pre><code>Log.d(&quot;Facebook-authorize&quot;, &quot;Login Success! access_token=&quot; + getAccessToken() + &quot; expires=&quot; + getAccessExpires());</code></pre></li> <li><p>Here is another example. A weather report for Android sent a user\'s location data to the log output as follows:</p> <pre><code>I/MyWeatherReport( 6483): Re-use MyWeatherReport data I/ ( 6483): GET JSON: http://example.com/smart/repo_piece.cgi?arc=0&amp;lat=26.209026&amp;lon=127.650803&amp;rad=50&amp;dir=-999&amp;lim=52&amp;category=1000</code></pre> <p>If a user is using Android OS 4.0 or before, other applications with READ_LOGS permission can obtain the user\'s location information without declaring ACCESS_FINE_LOCATION permission in the manifest file.</p></li> </ol>'

analiser2['risk'] = 3
vulnerability2['types'] = ["Static","Dynamic"]

analiser1['vulnerability'] = vulnerability1
analiser2['vulnerability'] = vulnerability2

file_data = {
    'created_on': '2017-03-03 09:17:31.568125+00:00',
    'device_token': 'None',
    'dynamic_status': 0,
    'icon_url': 'https://cdn.appknox.com/13cb5f99-0a67-43ae-89b6-35fe5bc01a78.png',
    'is_dynamic_done': False,
    'is_static_done': False,
    'manual': 0,
    'md5hash': '97d83c689f2cb0118e1901054165e8fe',
    'name': 'com.foo.bar',
    'sha1hash': 'd5341a898eb1d1e90a316d49e8f6b4f33ad08cf0',
    'updated_on': '2017-03-03 09:17:31.568149+00:00',
    'uuid': '04b8fa5d-2ea9-4055-b862-5b470640ffa2',
    'version': '1.0',
    'version_code': '1',
    'id': 29,
    'sorted_analyses': [analiser1, analiser2],
    'project': {
        'get_platform_display': "Some Platform"
    },
    'risk_count_critical': 12,
    'risk_count_high': 10,
    'risk_count_medium': 7,
    'risk_count_low': 8,
}

whitelabel_data = {
    'enabled': False,
    'name': 'Appknox',
    'logo': 'https://raw.githubusercontent.com/appknox/press-kit/master/logo/logo-dark-small.png'
}
