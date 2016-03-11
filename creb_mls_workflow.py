{
        'name': 'send_transactions_creb',
        'short_description': 'Send MLS listings to Brokermint',
        'full_description': '''For every listing of yours in <a href=\'/apps/creb_mls\'>CREB MLS</a> a new transaction is created in <a href=\'/apps/brokermint\'>Brokermint</a>, and appears as pending under “Incoming transactions” in the transaction list.
Listings will be processed starting from the date specified in workflow configuration.''',
        'about': 'Send MLS listings to Brokermint',
        'app_proxy': 'cn_mls_creb',
        'log_messages': {
            'Success': 'Success',
            'Fail': 'Failure'
        },
        'default_trigger': 'listings_updated',
        'connections': ['cn_mls_creb', 'cn_bm'],
        'configuration': [
            {
                "app": "cn_mls_creb",
                "title": "Enter listing",
                "label": "Trigger",
                "widgets": [
                    {"node": "header", "text": "Monitor from date"},
                    {'node': "date-picker", 'name': 'start_date'},
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
                ]
            },
            {"app": "cn_bm",
             "title": "Create transaction",
             "label": "Action",
             "widgets": []
             }
        ],
        'workflow': '{"generic_workflow_id": "%(generic_workflow_id)s", "user_id": %(user_id)d, "actions": [{"app_proxy": "cn_bm", "action": "send_transactions", "full_name_app":"BrokerMint", "mapping": "{\\"id\\":\\"Matrix_Unique_ID\\", \\"transaction_type\\": \\"TransactionType\\", \\"agent_id\\":\\"ListAgentMLSID\\", \\"agent_name\\": \\"ListAgentFullName\\", \\"address\\":\\"[StreetNumber , `\\\\\\" \\\\\\"`, StreetName , `\\\\\\" \\\\\\"`, StreetSuffix, `\\\\\\" \\\\\\"`, UnitNumber]\\", \\"city\\":\\"City\\", \\"state\\":\\"StateOrProvince\\", \\"price\\":\\"ListPrice\\", \\"status\\":\\"Status\\", \\"zip\\":\\"PostalCode\\", \\"custom_attributes.mls #\\":\\"MLSNumber\\", \\"custom_attributes.county\\":\\"Region\\", \\"custom_attributes.property type\\":\\"PropertyType\\", \\"custom_attributes.bedrooms\\":\\"BedsTotal\\", \\"custom_attributes.full baths\\":\\"BathsFull\\", \\"custom_attributes.half baths\\":\\"BathsHalf\\"}", "connect_id": "%(cn_bm_connect_id)s", "state": "full_connect"}], "trigger": "listings_updated", "connect_id": "%(cn_mls_creb_connect_id)s", "app_proxy": "cn_mls_creb", "full_name_app": "CREB MLS", "is_enabled": false, "trigger_id": "%(trigger_id)s", "status": "unused"}'
    },