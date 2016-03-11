{
    'name': 'send_transactions_mobmls',
    'short_description': 'Send MLS listings to Brokermint',
    'full_description': '''For every listing of yours in <a href=\'/apps/mobmls\'>MobMLS</a> a new transaction is created in <a href=\'/apps/brokermint\'>Brokermint</a>, and appears as pending under “Incoming transactions” in the transaction list.
Listings will be processed starting from the date specified in workflow configuration.''',
    'about': 'Send MLS listings to Brokermint',
    'app_proxy': 'cn_mls_mob',
    'log_messages': {
        'Success': 'Success',
        'Fail': 'Failure'
    },
    'default_trigger': 'listings_updated',
    'connections': ['cn_mls_mob', 'cn_bm'],
    'configuration': [
        {
            "app": "cn_mls_mob",
            "title": "Enter listing",
            "label": "Trigger",
            "widgets": [
                {"node": "header", "text": "Monitor from date"},
                {'node': "date-picker", 'name': 'start_date'},
                {"node": "validation-message", "text": "Date is required", "id": "start_date-error"},
                {"node": "header", "text": "Schedule"},
                {'node': 'only-schedule'},
                {
                    'value': 'listings_updated',
                    'name': 'trigger',
                    'node': 'input',
                    'type': 'text',
                    'wrapper-class': 'hidden',
                    'class': 'hidden'
                }
            ],
            "validations": [{"type": "required", "with": ["start_date"], "message": "#start_date-error"}]
        },

        {
            "app": "cn_bm",
            "title": "Create transaction",
            "label": "Action",
            "widgets": []
        }
    ],
        'workflow': '{"generic_workflow_id": "%(generic_workflow_id)s", "user_id": %(user_id)d, "actions": [{"app_proxy": "cn_bm", "action": "send_transactions", "full_name_app":"BrokerMint", "mapping": "{\\"id\\":\\"MLS_ACCT\\", \\"agent_id\\":\\"LA_CODE\\", \\"agent_name\\":\\"AGENT_OTHER_CONTACT_DESC\\", \\"street_number\\":\\"STREET_NUM\\", \\"street\\":\\"STREET_NAME\\", \\"unit_number\\":\\"UNIT_NUM\\", \\"address\\":\\"[STREET_NUM, `\\\\\\" \\\\\\"`, STREET_NAME, `\\\\\\" \\\\\\"`, UNIT_NUM]\\", \\"city\\":\\"CITY\\", \\"state\\":\\"STATE\\", \\"zip\\":\\"ZIP\\", \\"price\\":\\"LIST_PRICE\\", \\"status\\":\\"STATUS\\", \\"listing_date\\":\\"LIST_DATE\\", \\"expiration_date\\":\\"EXPIRE_DATE\\", \\"acceptance_date\\":\\"PENDING_DATE\\", \\"closing_date\\":\\"SOLD_DATE\\", \\"custom_attributes.mls #\\":\\"MLS_ACCT\\", \\"custom_attributes.county\\":\\"COUNTY\\", \\"custom_attributes.property type\\":\\"PROP_TYPE\\", \\"custom_attributes.area\\":\\"AREA\\", \\"custom_attributes.subdivision\\":\\"SUBDIVISION\\", \\"custom_attributes.listing type\\":\\"LISTING_TYPE\\", \\"custom_attributes.bedrooms\\":\\"BEDROOMS\\", \\"custom_attributes.full baths\\":\\"BATHS_FULL\\", \\"custom_attributes.half baths\\":\\"BATHS_HALF\\", \\"custom_attributes.floors\\":\\"FTR_FLOORS\\", \\"custom_attributes.heating\\":\\"FTR_HEATING\\", \\"custom_attributes.fireplace\\":\\"FTR_FIREPLACE\\", \\"custom_attributes.utilities\\":\\"FTR_UTILITIES\\", \\"custom_attributes.style\\":\\"FTR_STYLE\\", \\"custom_attributes.construction\\":\\"FTR_CONSTRUCTION\\", \\"custom_attributes.waterfront available\\":\\"FTR_WATERFRONT\\", \\"custom_attributes.show access\\":\\"FTR_SHOW_ACCESS\\", \\"custom_attributes.show appt\\":\\"FTR_SHOW_APPOINTMENT\\", \\"custom_attributes.description\\":\\"FTR_LOT_DESC\\", \\"custom_attributes.parcel #\\":\\"PARCEL_ID\\", \\"custom_attributes.legal description\\":\\"LEGALS\\", \\"custom_attributes.occupant\\":\\"OCCUPANT\\", \\"custom_attributes.commission to other broker\\":\\"COMM_OB\\", \\"custom_attributes.commission to other broker - type\\":\\"COMM_OB_TYPE\\", \\"custom_attributes.car shelter\\":\\"FTR_PARKING\\", \\"custom_attributes.porch\\":\\"FTR_PORCH\\"}", "connect_id": "%(cn_bm_connect_id)s", "state": "full_connect"}], "trigger": "listings_updated", "connect_id": "%(cn_mls_mob_connect_id)s", "app_proxy": "cn_mls_mob", "full_name_app": "MobMLS", "is_enabled": false, "trigger_id": "%(trigger_id)s", "status": "unused"}'
}