{
    'name': 'send_transactions',
    'short_description': 'Send MLS listings to Brokermint',
    'full_description': '''For every listing of yours in <a href=\'/apps/gardenstate_mls\'>Garden State MLS</a> a new transaction is created in <a href=\'/apps/brokermint\'>Brokermint</a>, and appears as pending under “Incoming transactions” in the transaction list.
Listings will be processed starting from the date specified in workflow configuration.''',
    'about': 'Send MLS listings to Brokermint',
    'app_proxy': 'cn_mls_gardenstate',
    'log_messages': {
        'Success': 'Success',
        'Fail': 'Failure'
    },
    'default_trigger': 'listings_updated',
    'connections': ['cn_mls_gardenstate', 'cn_bm'],
    'configuration': [
        {
            "app": "cn_mls_gardenstate",
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
    'workflow':'{ "generic_workflow_id": "%(generic_workflow_id)s", "user_id": %(user_id)d, "actions": [{"app_proxy": "cn_bm", "action": "send_transactions", "full_name_app":"BrokerMint", "mapping": "{\\"id\\":\\"ListingID\\",\\"agent_id\\":\\"AgentID\\",\\"agent_name\\":\\"ListAgentName\\", \\"address\\":\\"[StreetNumber , `\\\\\\" \\\\\\"`, StreetName , `\\\\\\" \\\\\\"`, UnitNumber]\\", \\"city\\":\\"City\\", \\"state\\":\\"State\\", \\"price\\":\\"[ListPrice, RentPrice]\\", \\"listing_date\\":\\"ListDate\\", \\"zip\\":\\"PostalCode\\", \\"status\\":\\"ListingStatus\\", \\"expiration_date\\":\\"ExpirationDate\\", \\"acceptance_date\\":\\"ContractDate\\", \\"closing_date\\":\\"CloseDate\\", \\"custom_attributes.mls #\\":\\"ListingID\\", \\"custom_attributes.county\\":\\"County\\", \\"custom_attributes.property type\\":\\"PropertyType\\", \\"custom_attributes.bedrooms\\":\\"Beds\\", \\"custom_attributes.full baths\\":\\"[NumUnitsFBath,BathsFullTotal,BathsFull]\\", \\"custom_attributes.half baths\\":\\"[NumUnitsHBath,BathsHalfTotal,BathsHalf]\\", \\"custom_attributes.show access\\":\\"ShowingInstructions\\", \\"custom_attributes.description\\":\\"Remarks\\", \\"custom_attributes.parcel #\\":\\"TaxID\\", \\"custom_attributes.legal description\\":\\"PublicRemarks\\"}", "connect_id": "%(cn_bm_connect_id)s", "state": "full_connect"}], "trigger": "listings_updated", "connect_id": "%(cn_mls_gardenstate_connect_id)s", "app_proxy": "cn_mls_gardenstate", "full_name_app": "MLS Garden State", "is_enabled": false, "trigger_id": "%(trigger_id)s", "status": "unused"}'
},