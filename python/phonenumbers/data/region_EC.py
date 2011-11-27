"""Auto-generated file, do not edit by hand. EC metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_EC = PhoneMetadata(id='EC', country_code=593, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[2-9]\\d{7}|1\\d{9,10}', possible_number_pattern='\\d{7,11}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='[2-7][2-7]\\d{6}', possible_number_pattern='\\d{7,8}', example_number='22123456'),
    mobile=PhoneNumberDesc(national_number_pattern='(?:69|[89]\\d)\\d{6}', possible_number_pattern='\\d{8}', example_number='99123456'),
    toll_free=PhoneNumberDesc(national_number_pattern='1800\\d{6,7}', possible_number_pattern='\\d{10,11}', example_number='18001234567'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='1(?:0[12]|12)|911', possible_number_pattern='\\d{3}', example_number='911'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d)(\\d{3})(\\d{4})', format='\\1 \\2-\\3', leading_digits_pattern=['[2-57]|6[2-7]'], national_prefix_formatting_rule='(0\\1)'),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['69|[89]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(1800)(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['1'], national_prefix_formatting_rule='\\1')],
    intl_number_format=[NumberFormat(pattern='(\\d)(\\d{3})(\\d{4})', format='\\1-\\2-\\3', leading_digits_pattern=['[2-57]|6[2-7]']),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['69|[89]']),
        NumberFormat(pattern='(1800)(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['1'])])
