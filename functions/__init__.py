
runtimes = [
	{
		"id": 1,
		"name": "Camera"
		
	},
	{
		"id": 2,
		"name": "Audio"
	},
	{
		"id": 3,
		"name": "Video"
	}
]

def get_runtimes(idx):
	for i in runtimes:
		if i['id'] == idx:
			return i
	return None