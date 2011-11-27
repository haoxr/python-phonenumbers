"""Auto-generated file, do not edit by hand. NG metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_NG = PhoneMetadata(id='NG', country_code=234, international_prefix='009',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-69]\\d{5,8}|[78]\\d{5,13}', possible_number_pattern='\\d{5,14}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='[12]\\d{6,7}|9\\d{7}|(?:4[023568]|5[02368]|6[02-469]|7[569]|8[2-9])\\d{6}|(?:4[47]|5[14579]|6[1578]|7[0-357])\\d{5,6}|(?:78|41)\\d{5}', possible_number_pattern='\\d{5,9}', example_number='12345678'),
    mobile=PhoneNumberDesc(national_number_pattern='(?:70(?:[3-9]\\d|2[1-9])|8(?:0[2-9]|1[0235689])\\d)\\d{6}', possible_number_pattern='\\d{10}', example_number='8021234567'),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{7,11}', possible_number_pattern='\\d{10,14}', example_number='80017591759'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='700\\d{7,11}', possible_number_pattern='\\d{10,14}', example_number='7001234567'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='199', possible_number_pattern='\\d{3}', example_number='199'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='([129])(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['[129]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([3-8]\\d)(\\d{3})(\\d{2,3})', format='\\1 \\2 \\3', leading_digits_pattern=['[3-6]|7(?:[1-79]|0[1-9])|8[2-9]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([78]\\d{2})(\\d{3})(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['70|8[01]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([78]00)(\\d{4})(\\d{4,5})', format='\\1 \\2 \\3', leading_digits_pattern=['[78]00'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([78]00)(\\d{5})(\\d{5,6})', format='\\1 \\2 \\3', leading_digits_pattern=['[78]00'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(78)(\\d{2})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['78'], national_prefix_formatting_rule='0\\1')])
