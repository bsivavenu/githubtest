## welcome message Quick Order + Favourite_Lunchpack + Proceed_With_Order + affirm
* get_started
   - utter_welcome_message
* quickreply{"quickreply_value":"Quick Order"}
   - slot{"quickreply_value":"Quick Order"}
   - utter_business_email
* email{"business_email": "ppreetham0@gmail.com"}
   - slot{"business_email": "ppreetham0@gmail.com"}
   - action_business_email
* Number{"Serial_Number": "1"}
   - slot{"Serial_Number": "1"}
   - action_serialNumber
* quickreply1{"quickreply_value1":"Favourite_Lunchpack"}
   - slot{"quickreply_value":"Favourite_Lunchpack"}
   - action_Order
   - slot{"child_id": "5678"}
   - slot{"order_id": "567834"}
* quickreply2{"quickreply_value2":"affirm"}
   - slot{"quickreply_value2":"affirm"}
   - action_which_date
* Number{"Serial_Number": "1"}
   - action_select_date
   - slot{"Date": "2020-09-19"}
* Number{"Serial_Number": "928829"}
  - action_validate_otp
*quickreply5{"quickreply_value5":"Number"}
   - action_feedback
   

## welcome message Quick Order + Favourite_Lunchpack + Proceed_With_Order + Deny 
* get_started
   - utter_welcome_message
* quickreply{"quickreply_value":"Quick Order"}
   - slot{"quickreply_value":"Quick Order"}
   - utter_business_email
* email{"business_email": "ppreetham0@gmail.com"}
   - slot{"business_email": "ppreetham0@gmail.com"}
   - action_business_email
* Number{"Serial_Number": "1"}
   - slot{"Serial_Number": "1"}
   - action_serialNumber
* quickreply1{"quickreply_value1":"Favourite_Lunchpack"}
   - slot{"quickreply_value":"Favourite_Lunchpack"}
   - action_Order
   - slot{"child_id": "5678"}
   - slot{"order_id": "567834"}
* quickreply2{"quickreply_value2":"deny"}
   - slot{"quickreply_value2":"deny"}
   - action_which_date
*quickreply5{"quickreply_value5":"Number"}
   - action_feedback
   
   
## welcome message Quick Order + LunchPack_LastOrder +Proceed_With_Order + deny
* get_started
   - utter_welcome_message
* quickreply{"quickreply_value":"Quick Order"}
   - slot{"quickreply_value":"Quick Order"}
   - utter_business_email
* email{"business_email": "ppreetham0@gmail.com"}
   - slot{"business_email": "ppreetham0@gmail.com"}
   - action_business_email
* Number{"Serial_Number": "1"}
   - slot{"Serial_Number": "1"}
   - action_serialNumber
* quickreply1{"quickreply_value1":"LunchPack_LastOrder"}
   - slot{"quickreply_value1":"LunchPack_LastOrder"}
   - action_Order
   - slot{"child_id": "45112"}
   - slot{"order_id": "567834"}
* quickreply2{"quickreply_value2":"deny"}
   - slot{"quickreply_value2":"deny"}
   - action_which_date
*quickreply5{"quickreply_value5":"Number"}
   - action_feedback
   
## welcome message Quick Order + LunchPack_LastOrder +Proceed_With_Order + affirm
* get_started
   - utter_welcome_message
* quickreply{"quickreply_value":"Quick Order"}
   - slot{"quickreply_value":"Quick Order"}
   - utter_business_email
* email{"business_email": "ppreetham0@gmail.com"}
   - slot{"business_email": "ppreetham0@gmail.com"}
   - action_business_email
* Number{"Serial_Number": "1"}
   - slot{"Serial_Number": "1"}
   - action_serialNumber
* quickreply1{"quickreply_value1":"LunchPack_LastOrder"}
   - slot{"quickreply_value1":"LunchPack_LastOrder"}
   - action_Order
   - slot{"child_id": "45112"}
   - slot{"order_id": "567834"}
* quickreply2{"quickreply_value2":"affirm"}
   - slot{"quickreply_value2":"affirm"}
   - action_which_date
* Number{"Serial_Number": "1"}
   - action_select_date
* Number{"Serial_Number": "928829"}
   - action_validate_otp
*quickreply5{"quickreply_value5":"Number"}
   - action_feedback

   
   
## welcome message Quick Order + custom_lunchpack
* get_started
   - utter_welcome_message
* quickreply{"quickreply_value":"Quick Order"}
   - slot{"quickreply_value":"Quick Order"}
   - utter_business_email
* email{"business_email": "ppreetham0@gmail.com"}
   - slot{"business_email": "ppreetham0@gmail.com"}
   - action_business_email
* Number{"Serial_Number": "1"}
   - slot{"Serial_Number": "1"}
   - action_serialNumber
* quickreply1{"quickreply_value1":"custom_lunchpack"}
   - slot{"quickreply_value1":"custom_lunchpack"}
   - action_Order


   
   
## welcome message Show Current Offers + Yes +quick order+Favourite_Lunchpack +affirm
* get_started
   - utter_welcome_message
* quickreply{"quickreply_value":"Show Current Offers"}
   - slot{"quickreply_value":"Show Current Offers"}
   - utter_business_email
* email{"business_email": "ppreetham0@gmail.com"}
   - slot{"business_email": "ppreetham0@gmail.com"}
   - action_business_email
* quickreply6{"quickreply_value6":"affirm"}
   - slot{"quickreply_value6":"affirm"}
   - action_Please_go_quickorder
* Number{"Serial_Number": "1"}
   - slot{"Serial_Number": "1"}
   - action_serialNumber
* quickreply1{"quickreply_value1":"Favourite_Lunchpack"}
   - slot{"quickreply_value":"Favourite_Lunchpack"}
   - action_Order
   - slot{"child_id": "5678"}
   - slot{"order_id": "567834"}
* quickreply2{"quickreply_value2":"affirm"}
   - slot{"quickreply_value2":"affirm"}
   - action_which_date
* Number{"Serial_Number": "1"}
   - action_select_date
   - slot{"Date": "2020-09-19"}
* Number{"Serial_Number": "928829"}
  - action_validate_otp
*quickreply5{"quickreply_value5":"Number"}
   - action_feedback
   
   
## welcome message Show Current Offers + Yes +quick order+Favourite_Lunchpack +deny
* get_started
   - utter_welcome_message
* quickreply{"quickreply_value":"Show Current Offers"}
   - slot{"quickreply_value":"Show Current Offers"}
   - utter_business_email
* email{"business_email": "ppreetham0@gmail.com"}
   - slot{"business_email": "ppreetham0@gmail.com"}
   - action_business_email
* quickreply6{"quickreply_value6":"affirm"}
   - slot{"quickreply_value6":"affirm"}
   - action_Please_go_quickorder
* Number{"Serial_Number": "1"}
   - slot{"Serial_Number": "1"}
   - action_serialNumber
* quickreply1{"quickreply_value1":"Favourite_Lunchpack"}
   - slot{"quickreply_value":"Favourite_Lunchpack"}
   - action_Order
   - slot{"child_id": "5678"}
   - slot{"order_id": "567834"}
* quickreply2{"quickreply_value2":"deny"}
   - slot{"quickreply_value2":"deny"}
   - action_which_date
*quickreply5{"quickreply_value5":"Number"}
   - action_feedback
   
   
## welcome message Show Current Offers + Yes +quick order+LunchPack_LastOrder + deny
* get_started
   - utter_welcome_message
* quickreply{"quickreply_value":"Show Current Offers"}
   - slot{"quickreply_value":"Show Current Offers"}
   - utter_business_email
* email{"business_email": "ppreetham0@gmail.com"}
   - slot{"business_email": "ppreetham0@gmail.com"}
   - action_business_email
* quickreply6{"quickreply_value6":"affirm"}
   - slot{"quickreply_value6":"affirm"}
   - action_Please_go_quickorder
* Number{"Serial_Number": "1"}
   - slot{"Serial_Number": "1"}
   - action_serialNumber
* quickreply1{"quickreply_value1":"LunchPack_LastOrder"}
   - slot{"quickreply_value1":"LunchPack_LastOrder"}
   - action_Order
   - slot{"child_id": "45112"}
   - slot{"order_id": "567834"}
* quickreply2{"quickreply_value2":"deny"}
   - slot{"quickreply_value2":"deny"}
   - action_which_date
*quickreply5{"quickreply_value5":"Number"}
   - action_feedback
   
   
## welcome message Show Current Offers + Yes +quick order+LunchPack_LastOrder + affirm
* get_started
   - utter_welcome_message
* quickreply{"quickreply_value":"Show Current Offers"}
   - slot{"quickreply_value":"Show Current Offers"}
   - utter_business_email
* email{"business_email": "ppreetham0@gmail.com"}
   - slot{"business_email": "ppreetham0@gmail.com"}
   - action_business_email
* quickreply6{"quickreply_value6":"affirm"}
   - slot{"quickreply_value6":"affirm"}
   - action_Please_go_quickorder
* Number{"Serial_Number": "1"}
   - slot{"Serial_Number": "1"}
   - action_serialNumber
* quickreply1{"quickreply_value1":"LunchPack_LastOrder"}
   - slot{"quickreply_value1":"LunchPack_LastOrder"}
   - action_Order
   - slot{"child_id": "45112"}
   - slot{"order_id": "567834"}
* quickreply2{"quickreply_value2":"affirm"}
   - slot{"quickreply_value2":"affirm"}
   - action_which_date
* Number{"Serial_Number": "1"}
   - action_select_date
   - slot{"Date": "2020-09-19"}
* Number{"Serial_Number": "928829"}
  - action_validate_otp
*quickreply5{"quickreply_value5":"Number"}
   - action_feedback
   
   
   
## welcome message Show Current Offers
* get_started
   - utter_welcome_message
* quickreply{"quickreply_value":"Show Current Offers"}
   - slot{"quickreply_value":"Show Current Offers"}
   - utter_business_email
* email{"business_email": "ppreetham0@gmail.com"}
   - slot{"business_email": "ppreetham0@gmail.com"}
   - action_business_email
* quickreply6{"quickreply_value6":"deny"}
   - slot{"quickreply_value6":"deny"}
   - utter_feedback
*quickreply5{"quickreply_value5":"Number"}
   - action_feedback
   


## welcome message status_of_order + Deny
* get_started
   - utter_welcome_message
* quickreply{"quickreply_value":"status_of_my_order"}
   - slot{"quickreply_value":"status_of_my_order"}
   - utter_business_email
* email{"business_email": "ppreetham0@gmail.com"}
   - slot{"business_email": "ppreetham0@gmail.com"}
   - action_business_email
* quickreply7{"quickreply_value7":"deny"}
   - slot{"quickreply_value7":"deny"}
   - action_for_location
*quickreply5{"quickreply_value5":"Number"}
   - action_feedback
   
## welcome message status_of_order + affirm
* get_started
   - utter_welcome_message
* quickreply{"quickreply_value":"status_of_my_order"}
   - slot{"quickreply_value":"status_of_my_order"}
   - utter_business_email
* email{"business_email": "ppreetham0@gmail.com"}
   - slot{"business_email": "ppreetham0@gmail.com"}
   - action_business_email
* quickreply7{"quickreply_value7":"affirm"}
   - slot{"quickreply_value7":"affirm"}
   - action_for_location
* Number{"Serial_Number": "1"}
   - slot{"Serial_Number": "1"}
   - action_serialNumber
*quickreply5{"quickreply_value5":"Number"}
   - action_feedback
   
   
   
   
## welcome message todays_Lunchbox_details
* get_started
   - utter_welcome_message
* quickreply{"quickreply_value":"todays_Lunchbox_details"}
   - slot{"quickreply_value":"todays_Lunchbox_details"}
   - utter_business_email
* email{"business_email": "ppreetham0@gmail.com"}
   - slot{"business_email": "ppreetham0@gmail.com"}
   - action_business_email
*quickreply5{"quickreply_value5":"Number"}
   - action_feedback
  
   
   
## welcome message Order_placed_tommorrow + Yes +quick order+Favourite_Lunchpack +affirm
* get_started
   - utter_welcome_message
* quickreply{"quickreply_value":"Order_placed_tommorrow"}
   - slot{"quickreply_value":"whether order placed for tomorrow"}	
    - utter_business_email
* email{"business_email": "ppreetham0@gmail.com"}
  - slot{"business_email": "ppreetham0@gmail.com"}
  - action_business_email
* quickreply7{"quickreply_value7":"affirm"}
   - slot{"quickreply_value7":"affirm"}
   - action_Please_go_quickorder
* Number{"Serial_Number": "1"}
   - slot{"Serial_Number": "1"}
   - action_serialNumber
* quickreply1{"quickreply_value1":"Favourite_Lunchpack"}
   - slot{"quickreply_value":"Favourite_Lunchpack"}
   - action_Order
   - slot{"child_id": "5678"}
   - slot{"order_id": "567834"}
* quickreply2{"quickreply_value2":"affirm"}
   - slot{"quickreply_value2":"affirm"}
   - action_which_date
* Number{"Serial_Number": "1"}
   - action_select_date
   - slot{"Date": "2020-09-19"}
* Number{"Serial_Number": "928829"}
  - action_validate_otp
*quickreply5{"quickreply_value5":"Number"}
   - action_feedback
   
## welcome message order_placed_tommorrow + Yes +quick order+Favourite_Lunchpack +deny
* get_started
   - utter_welcome_message
* quickreply{"quickreply_value":"Order_placed_tommorrow"}
   - slot{"quickreply_value":"whether order placed for tomorrow"}	
    - utter_business_email
* email{"business_email": "ppreetham0@gmail.com"}
  - slot{"business_email": "ppreetham0@gmail.com"}
  - action_business_email
* quickreply7{"quickreply_value7":"affirm"}
   - slot{"quickreply_value7":"affirm"}
   - action_Please_go_quickorder
* Number{"Serial_Number": "1"}
   - slot{"Serial_Number": "1"}
   - action_serialNumber
* quickreply1{"quickreply_value1":"Favourite_Lunchpack"}
   - slot{"quickreply_value":"Favourite_Lunchpack"}
   - action_Order
   - slot{"child_id": "5678"}
   - slot{"order_id": "567834"}
* quickreply2{"quickreply_value2":"deny"}
   - slot{"quickreply_value2":"deny"}
   - action_which_date
*quickreply5{"quickreply_value5":"Number"}
   - action_feedback
   
   
## welcome message Show order_placed_tommorrow + Yes +quick order+LunchPack_LastOrder + deny
* get_started
   - utter_welcome_message
* quickreply{"quickreply_value":"Order_placed_tommorrow"}
   - slot{"quickreply_value":"whether order placed for tomorrow"}	
    - utter_business_email
* email{"business_email": "ppreetham0@gmail.com"}
  - slot{"business_email": "ppreetham0@gmail.com"}
  - action_business_email
* quickreply7{"quickreply_value7":"affirm"}
   - slot{"quickreply_value7":"affirm"}
   - action_Please_go_quickorder
* Number{"Serial_Number": "1"}
   - slot{"Serial_Number": "1"}
   - action_serialNumber
* quickreply1{"quickreply_value1":"LunchPack_LastOrder"}
   - slot{"quickreply_value1":"LunchPack_LastOrder"}
   - action_Order
   - slot{"child_id": "45112"}
   - slot{"order_id": "567834"}
* quickreply2{"quickreply_value2":"deny"}
   - slot{"quickreply_value2":"deny"}
   - action_which_date
*quickreply5{"quickreply_value5":"Number"}
   - action_feedback
   
   
## welcome message Show order_placed_tommorrow + Yes +quick order+LunchPack_LastOrder + affirm
* get_started
   - utter_welcome_message
* quickreply{"quickreply_value":"Order_placed_tommorrow"}
   - slot{"quickreply_value":"whether order placed for tomorrow"}	
   - utter_business_email
* email{"business_email": "ppreetham0@gmail.com"}
   - slot{"business_email": "ppreetham0@gmail.com"}
   - action_business_email
* quickreply7{"quickreply_value7":"affirm"}
   - slot{"quickreply_value7":"affirm"}
   - action_Please_go_quickorder
* Number{"Serial_Number": "1"}
   - slot{"Serial_Number": "1"}
   - action_serialNumber
* quickreply1{"quickreply_value1":"LunchPack_LastOrder"}
   - slot{"quickreply_value1":"LunchPack_LastOrder"}
   - action_Order
   - slot{"child_id": "45112"}
   - slot{"order_id": "567834"}
* quickreply2{"quickreply_value2":"affirm"}
   - slot{"quickreply_value2":"affirm"}
   - action_which_date
* Number{"Serial_Number": "1"}
   - action_select_date
   - slot{"Date": "2020-09-19"}
* Number{"Serial_Number": "928829"}
  - action_validate_otp
*quickreply5{"quickreply_value5":"Number"}
   - action_feedback
   
## welcome message lunchpacks_available + Yes +quick order+Favourite_Lunchpack +affirm
* get_started
   - utter_welcome_message
* quickreply{"quickreply_value":"lunchpacks_available"}
   - slot{"quickreply_value":"Want to know about lunchpacks available"}
   - utter_business_email
* email{"business_email": "ppreetham0@gmail.com"}
   - slot{"business_email": "ppreetham0@gmail.com"}
   - action_business_email
* Number{"Serial_Number": "1"}
   - slot{"Serial_Number": "1"}
   - action_serialNumber
* quickreply6{"quickreply_value6":"affirm"}
   - slot{"quickreply_value6":"affirm"}
   - action_Please_go_quickorder
* Number{"Serial_Number": "1"}
   - slot{"Serial_Number": "1"}
   - action_serialNumber
* quickreply1{"quickreply_value1":"Favourite_Lunchpack"}
   - slot{"quickreply_value":"Favourite_Lunchpack"}
   - action_Order
   - slot{"child_id": "5678"}
   - slot{"order_id": "567834"}
* quickreply2{"quickreply_value2":"affirm"}
   - slot{"quickreply_value2":"affirm"}
   - action_which_date
* Number{"Serial_Number": "1"}
   - action_select_date
   - slot{"Date": "2020-09-19"}
* Number{"Serial_Number": "928829"}
  - action_validate_otp
*quickreply5{"quickreply_value5":"Number"}
   - action_feedback

## welcome message lunchpacks_available + Yes +quick order+Favourite_Lunchpack +deny
* get_started
   - utter_welcome_message
* quickreply{"quickreply_value":"lunchpacks_available"}
   - slot{"quickreply_value":"Want to know about lunchpacks available"}
   - utter_business_email
* email{"business_email": "ppreetham0@gmail.com"}
   - slot{"business_email": "ppreetham0@gmail.com"}
   - action_business_email
* Number{"Serial_Number": "1"}
   - slot{"Serial_Number": "1"}
   - action_serialNumber
* quickreply6{"quickreply_value6":"affirm"}
   - slot{"quickreply_value6":"affirm"}
   - action_Please_go_quickorder
* Number{"Serial_Number": "1"}
   - slot{"Serial_Number": "1"}
   - action_serialNumber
* quickreply1{"quickreply_value1":"Favourite_Lunchpack"}
   - slot{"quickreply_value":"Favourite_Lunchpack"}
   - action_Order
   - slot{"child_id": "5678"}
   - slot{"order_id": "567834"}
* quickreply2{"quickreply_value2":"deny"}
   - slot{"quickreply_value2":"deny"}
   - action_which_date
*quickreply5{"quickreply_value5":"Number"}
   - action_feedback
   
## welcome message lunchpacks_available + Yes +quick order+LunchPack_LastOrder + deny
* get_started
   - utter_welcome_message
* quickreply{"quickreply_value":"lunchpacks_available"}
   - slot{"quickreply_value":"Want to know about lunchpacks available"}
   - utter_business_email
* email{"business_email": "ppreetham0@gmail.com"}
   - slot{"business_email": "ppreetham0@gmail.com"}
   - action_business_email
* Number{"Serial_Number": "1"}
   - slot{"Serial_Number": "1"}
   - action_serialNumber
* quickreply6{"quickreply_value6":"affirm"}
   - slot{"quickreply_value6":"affirm"}
   - action_Please_go_quickorder
* Number{"Serial_Number": "1"}
   - slot{"Serial_Number": "1"}
   - action_serialNumber
* quickreply1{"quickreply_value1":"LunchPack_LastOrder"}
   - slot{"quickreply_value1":"LunchPack_LastOrder"}
   - action_Order
   - slot{"child_id": "45112"}
   - slot{"order_id": "567834"}
* quickreply2{"quickreply_value2":"deny"}
   - slot{"quickreply_value2":"deny"}
   - action_which_date
*quickreply5{"quickreply_value5":"Number"}
   - action_feedback
   
## welcome message lunchpacks_available + Yes +quick order+LunchPack_LastOrder + affirm
* get_started
   - utter_welcome_message
* quickreply{"quickreply_value":"lunchpacks_available"}
   - slot{"quickreply_value":"Want to know about lunchpacks available"}
   - utter_business_email
* email{"business_email": "ppreetham0@gmail.com"}
   - slot{"business_email": "ppreetham0@gmail.com"}
   - action_business_email
* Number{"Serial_Number": "1"}
   - slot{"Serial_Number": "1"}
   - action_serialNumber
* quickreply6{"quickreply_value6":"affirm"}
   - slot{"quickreply_value6":"affirm"}
   - action_Please_go_quickorder
* Number{"Serial_Number": "1"}
   - slot{"Serial_Number": "1"}
   - action_serialNumber
* quickreply1{"quickreply_value1":"LunchPack_LastOrder"}
   - slot{"quickreply_value1":"LunchPack_LastOrder"}
   - action_Order
   - slot{"child_id": "45112"}
   - slot{"order_id": "567834"}
* quickreply2{"quickreply_value2":"affirm"}
   - slot{"quickreply_value2":"affirm"}
   - action_which_date
* Number{"Serial_Number": "1"}
   - action_select_date
   - slot{"Date": "2020-09-19"}
* Number{"Serial_Number": "928829"}
  - action_validate_otp
*quickreply5{"quickreply_value5":"Number"}
   - action_feedback   
   
## welcome message lunchpacks_available
* get_started
   - utter_welcome_message
* quickreply{"quickreply_value":"lunchpacks_available"}
   - slot{"quickreply_value":"Want to know about lunchpacks available"}
   - utter_business_email
* email{"business_email": "ppreetham0@gmail.com"}
   - slot{"business_email": "ppreetham0@gmail.com"}
   - action_business_email
* Number{"Serial_Number": "1"}
   - slot{"Serial_Number": "1"}
   - action_serialNumber
 
## welcome message cancel_order_for_next_friday + affirm
* get_started
   - utter_welcome_message
* quickreply{"quickreply_value":"cancel_order_for_next_friday"}
   - slot{"quickreply_value":"cancel your order for Next Friday"}
   - utter_business_email
* email{"business_email": "ppreetham0@gmail.com"}
   - slot{"business_email": "ppreetham0@gmail.com"}
   - action_business_email
* Number{"Serial_Number": "3"}
   - slot{"Serial_Number": "3"}
   - slot{"order_detail_id": "45678"}
   - action_serialNumber
* quickreply4{"quickreply_value4":"affirm"}
   - slot{"quickreply_value4":"affirm"}   
   - action_validate_otp
* quickreply5{"quickreply_value5":"Number"}
   - action_feedback   
 
## welcome message cancel_order_for_next_friday + deny
* get_started
   - utter_welcome_message
* quickreply{"quickreply_value":"cancel_order_for_next_friday"}
   - slot{"quickreply_value":"cancel your order for Next Friday"}
   - utter_business_email
* email{"business_email": "ppreetham0@gmail.com"}
   - slot{"business_email": "ppreetham0@gmail.com"}
   - action_business_email
* Number{"Serial_Number": "3"}
   - slot{"Serial_Number": "3"}
   - slot{"order_detail_id": "45678"}
   - action_serialNumber
* quickreply4{"quickreply_value4":"deny"}
   - slot{"quickreply_value4":"deny"}   
   - action_validate_otp
* quickreply5{"quickreply_value5":"Number"}
   - action_feedback  
   
  
 