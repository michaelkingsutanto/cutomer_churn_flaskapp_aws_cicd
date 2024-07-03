def format_model_inputs(input_dict):
    age = int(input_dict['age'])
    tenure_months = int(input_dict['tenure_months'])
    num_referrals = int(input_dict['num_referrals'])
    num_dependents = int(input_dict['num_dependents'])
    total_monthly_fee = float(input_dict['total_monthly_fee'])
    married = input_dict['married']
    contract_type = input_dict['contract_type']
    zip_code = input_dict['zip_code']
    internet_type = input_dict['internet_type']
    payment_method = input_dict['payment_method']


    return {
        'contract_type': contract_type, 
        'num_referrals': num_referrals,
        'num_dependents': num_dependents,
        'internet_type': internet_type,
        'age': age, 
        'tenure_months': tenure_months,
        'zip_code': zip_code,
        'payment_method': payment_method,
        'total_monthly_fee': total_monthly_fee,
        'married': married
    }

def validate(input_dict):
    errors = []

    required_fields = [
        'contract_type', 
        'num_referrals',
        'num_dependents',
        'internet_type',
        'age', 
        'tenure_months',
        'zip_code',
        'payment_method',
        'total_monthly_fee',
        'married']

    for field in required_fields:

        if field not in input_dict:
            errors.append(f'{field} not found in request.')

        if field in ['age', 'tenure_months', 'num_referrals', 'num_dependents'] and type(input_dict[field]) != int \
                and not input_dict[field].isnumeric():
            errors.append(f'age, tenure_months, num_referrals, and num_dependents fields must be int type.')

        elif field in ['total_monthly_fee'] and type(input_dict[field]) != float:
            try:
                float(input_dict[field])
            except ValueError:
                errors.append(f'total_monthly_fee field must be numeric.')

    return errors