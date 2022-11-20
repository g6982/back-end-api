# See LICENSE file for full copyright and licensing details.

{
    "name": "Partner Auth With Otp",
    "version": "15.0.1.0.0",
    "author": "@The-Kadweka",
    "website": "",
    "category": "tools",
    "license": "AGPL-3",
    "summary": "A module to allow authentication with email otp in odoo",
    "complexity": "easy",
    "images": ["static/description/exam_banner.png"],
    "depends": ["base"],
    "data": [
        'security/ir.model.access.csv',
        'views/access_configuration.xml'],
    "demo": [],
    "installable": True,
    "application": True,
}
