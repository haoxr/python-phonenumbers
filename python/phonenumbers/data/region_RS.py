"""Auto-generated file, do not edit by hand. RS metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_RS = PhoneMetadata(id='RS', country_code=381, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-36-9]\\d{4,11}', possible_number_pattern='\\d{5,12}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='[1-3]\\d{6,11}', possible_number_pattern='\\d{5,12}', example_number='101234567'),
    mobile=PhoneNumberDesc(national_number_pattern='6(?:[0-689]|7\\d)\\d{6,7}', possible_number_pattern='\\d{8,10}', example_number='601234567'),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{3,9}', possible_number_pattern='\\d{6,12}', example_number='80012345'),
    premium_rate=PhoneNumberDesc(national_number_pattern='(?:90[0169]|78\\d)\\d{3,7}', possible_number_pattern='\\d{6,12}', example_number='90012345'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='7[06]\\d{4,10}', possible_number_pattern='\\d{6,12}', example_number='700123456'),
    emergency=PhoneNumberDesc(national_number_pattern='112|9[234]', possible_number_pattern='\\d{2,3}', example_number='112'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='([23]\\d{2})(\\d{4,9})', format='\\1 \\2', leading_digits_pattern=['(?:2[389]|39)0'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([1-3]\\d)(\\d{5,10})', format='\\1 \\2', leading_digits_pattern=['1|2(?:[0-24-7]|[389][1-9])|3(?:[0-8]|9[1-9])'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(6\\d)(\\d{6,8})', format='\\1 \\2', leading_digits_pattern=['6'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([89]\\d{2})(\\d{3,9})', format='\\1 \\2', leading_digits_pattern=['[89]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(7[26])(\\d{4,9})', format='\\1 \\2', leading_digits_pattern=['7[26]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(7[08]\\d)(\\d{4,9})', format='\\1 \\2', leading_digits_pattern=['7[08]'], national_prefix_formatting_rule='0\\1')])
