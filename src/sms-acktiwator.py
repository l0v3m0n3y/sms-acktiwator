import requests
class Client():
	def __init__(self,key: str):
		self.api="https://sms-acktiwator.ru/api"
		self.api_key=key
	def numbers_status(self,code: str):
		return requests.get(f"{self.api}/numbersstatus/{self.api_key}?code={code}").json()
	def get_balance(self):
		return requests.get(f"{self.api}/getbalance/{self.api_key}").json()
	def get_number(self,service: str,code: str):
		return requests.get(f"{self.api}/getnumber/{self.api_key}?id={service}&code={code}").json()
	def countries(self):
		return requests.get(f"{self.api}/countries/{self.api_key}").json()
	def get_services(self):
		return requests.get(f"{self.api}/getservices/{self.api_key}").json()
	def get_status(self,id: str):
		return requests.get(f"{self.api}/getstatus/{self.api_key}?id={id}").json()
	def all_sms(self,id: str):
		return requests.get(f"{self.api}/all-sms/{self.api_key}?id={id}").json()
	def get_latest_code(self,id: str):
		return requests.get(f"{self.api}/getlatestcode/{self.api_key}?id={id}").json()
	def play(self,id: str):
		return requests.get(f"{self.api}/play/{self.api_key}?id={id}").json()
	def set_status(self,id: str,status: str):
		return requests.get(f"{self.api}/setstatus/{self.api_key}?id={id}&{status}={status}").json()
	def get_full_numbers(self):
		return requests.get(f"{self.api}/getfullnumbers/{self.api_key}").json()
	def full_numbers(self,code: str,tarif: str):
		return requests.get(f"{self.api}/getfullnumber/{self.api_key}?code={code}&tarif={tarif}").json()
	def send_enable_sim(self,id: str):
		return requests.get(f"{self.api}/send-enable-sim/{self.api_key}?id={id}").json()
	def send_disable_sim(self,id: str):
		return requests.get(f"{self.api}/send-disable-sim/{self.api_key}?id={id}").json()
	def get_all_sms(self,phone: str):
		return requests.get(f"{self.api}/getallsmsofnumber/{self.api_key}?phone={phone}").json()
	def get_all_tarifs(self):
		return requests.get(f"{self.api}/getalltarifs/{self.api_key}").json()
	def rebuy_number(self,id: str, tarif: str):
		return requests.get(f"{self.api}/rebuynumber/{self.api_key}?id={id}&tarif={tarif}").json()