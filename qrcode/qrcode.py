import segno
from segno import helpers

def wifi_dict():
	wifi_settings = {
		'ssid':'TheThirdOne',
		'password' :'@pass#1wd',
		'security' :'WPA2',
		}
	wifi = helpers.make_wifi(**wifi_settings)
	wifi.save("rssid.png", dark="red", light = "black", scale = 10)

def wifi():
	qrcode = helpers.make_wifi(ssid='TheThirdOne', password='@pass#1wd', security='WPA2')
	qrcode.designator
	'3-M'
	qrcode.save('bssid.png', scale=10)
	qrcode.save("pssid.png", dark="yellow", light = "black", scale = 10)

def text():
	data = segno.make_qr('All You')
	data.save('txt.png', scale=10)

def video():
	lnk = segno.make('https://www.youtube.com/@MxRPlays')
	lnk.save('MxRPlays.png', dark = 'black', data_dark='red', scale=10)

def micro():
	micro_qrcode = segno.make_qr('_hil', error='q')
	micro_qrcode.save('rain.png', dark='darkred', data_dark='red', scale=10)

def contact():
	from segno import helpers
	qrcode = helpers.make_mecard(name='Khlu Klua', email='Khluklua@gmail.com', phone='+123456789')
	qrcode.designator
	'3-L'
	qrcode.save('contact.png', dark='black', data_dark='orange', scale=8)
	# Some params accept multiple values, like email, phone, url
	qrcode2 = helpers.make_mecard(name='Kahlulu Kahlua', 
                             email=('me@example1.com', 'email@example2.com'),
                             url=['http://www.example1.com', 'https://example2.come/~olu'])
	qrcode2.save('mycontact.png', dark='black', data_dark='purple', scale=8)

if __name__ == '__main__':
	#wifi_dict()
	#wifi()
	#text()
	#video()
	#micro()
	#contact()
