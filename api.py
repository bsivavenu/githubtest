import requests 
import json

class API:
	def __init__(self):
		self.base_url='https://cornerstonesolutions.ai/subs/'
	
	

	def verify_user(self,data):
		verify_user_api=self.base_url+"api_verify_user"
		response = requests.post(url=verify_user_api,data=json.dumps(data))
		r = response.json()
		return (r['status'])

	def Order_status(self,data):
		order_status_api=self.base_url+"api_status_last_order"
		response = requests.post(url=order_status_api,data=json.dumps(data))
		result = response.json()
		return result
		# details = []
		# order_ids = []
		# for record in result['data']:
			# if record['order_status'] == 'pending':
				# order_ids.append(record['order_detail_id'])
				# details.append('order id: '+ str(record['order_detail_id'])+' order status: '+str(record['order_status']+' delivery date: '+str(record['delivery_date'])))
		# return order_ids,details

	def Lunch_box_details(self,data):
		today_lunch_detail_api=self.base_url+"api_today_lunch_detail"
		response = requests.post(url=today_lunch_detail_api,data=json.dumps(data))
		r = response.json()
		return r

	def Order_for_tomorrow(self,data):
		check_tomorrow_order_api=self.base_url+"api_check_tomorrow_order"
		response = requests.post(url=check_tomorrow_order_api,data=json.dumps(data))
		r = response.json()
		return r

	def cancel_my_order(self,data):
		cancel_order_api=self.base_url+"api_cancel_order"	
		response = requests.post(url=cancel_order_api,data=json.dumps(data))
		r = response.json()
		return r

	def check_tomorrow_order(self,data):
		check_tomorrow_order_api=self.base_url+"/api_check_tomorrow_order"	
		response = requests.post(url=check_tomorrow_order_api,data=json.dumps(data))
		r = response.json()
		return r

	def available_lunch_pack(self,data):
		available_lunch_pack_api=self.base_url+"/api_available_lunch_pack"	
		response = requests.post(url=available_lunch_pack_api,data=json.dumps(data))
		r = response.json()
		return r

	def offers_list(self,data):
		offers_list_api=self.base_url+"/api_offers_list"	
		response = requests.post(url=offers_list_api,data=json.dumps(data))
		r = response.json()
		return r

	def child_list(self,data):
		child_list_api=self.base_url+"/api_child_list"	
		response = requests.post(url=child_list_api,data=json.dumps(data))
		r = response.json()
		return r

	def child_last_order(self,data):
		child_last_order_api=self.base_url+"/api_child_last_order"	
		response = requests.post(url=child_last_order_api,data=json.dumps(data))
		r = response.json()
		return r

	def child_favourite_pack(self,data):
		child_favourite_pack_api=self.base_url+"/api_child_favourite_pack"	
		response = requests.post(url=child_favourite_pack_api,data=json.dumps(data))
		r = response.json()
		return r

	def otp_genrate(self,data):
		otp_genrate_api=self.base_url+"/api_otp_genrate"	
		response = requests.post(url=otp_genrate_api,data=json.dumps(data))
		r = response.json()
		return r

	def child_order_availalable(self,data):
		child_order_availalable_api=self.base_url+"/api_child_order_availalable"	
		response = requests.post(url=child_order_availalable_api,data=json.dumps(data))
		r = response.json()
		return r

	def lunch_pack_detail(self,data):
		lunch_pack_detail_api=self.base_url+"/api_lunch_pack_detail"	
		response = requests.post(url=lunch_pack_detail_api,data=json.dumps(data))
		r = response.json()
		return r

	def place_order(self,data):
		place_order_api=self.base_url+"/api_place_order"	
		response = requests.post(url=place_order_api,data=json.dumps(data))
		r = response.json()
		return r
	
	def feedback(self,data):
		place_order_api=self.base_url+"/api_save_feedback"	
		response = requests.post(url=feedback_api,data=json.dumps(data))
		r = response.json()
		return r
		
	def all_order_status(self,data):
		order_status_api=self.base_url+"/api_status_last_order"
		response = requests.post(url=order_status_api,data=json.dumps(data))
		result = response.json()
		return result










