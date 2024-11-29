# validation_settings.py

VALIDATORS = {
    'EstateViewSet': {
        'create': [
            'main_app.request_validator.estate_validator_1.EstateValidator1',
            'main_app.request_validator.estate_validator_2.EstateValidator2',
        ],
        'update': [
            'main_app.request_validator.estate_validator_2.EstateValidator2',
        ],
        'partial_update':[
            'main_app.request_validator.estate_validator_1.EstateValidator1'
        ]
    }
}
