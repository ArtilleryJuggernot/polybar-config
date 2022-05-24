import python_weather
import asyncio
import sys
async def getweather():
	client = python_weather.Client(format=python_weather.IMPERIAL)	
	weather = await client.find("Tokyo")
	temp = weather.current.temperature
	temp = (temp - 34) * 5/9
	sys.stout.write(temp)
	await client.close()

if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	loop.run_until_complete(getweather())
	
