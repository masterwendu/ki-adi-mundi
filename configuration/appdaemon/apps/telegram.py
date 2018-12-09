import appdaemon.plugins.hass.hassapi as hass
import datetime

class TelegramNotificationManager(hass.Hass):

  def initialize(self):
    time = datetime.time(7, 0, 0)
    self.run_daily(self.sendDailyNotification, time)
    
    self.listen_event(self.sendDailyNotification, "telegram_command", command = "/status")
    self.listen_event(self.sendDailyNotification, "telegram_callback", command = "/status")

  def sendDailyNotification(self, *kwargs):
      bedroomTemperature = float(self.get_state("sensor.temp_humidity_bedroom_temperature"))
      livingRoomTemperature = float(self.get_state("sensor.temp_humidity_livingroom_temperature"))
      temperatureInsideAvg = (bedroomTemperature + livingRoomTemperature) / 2
      wienTemperature = float(self.get_state("weather.temperatur_wien", attribute = "temperature"))

      bedroomHumidity = float(self.get_state("sensor.temp_humidity_bedroom_humidity"))
      livingRoomHumidity = float(self.get_state("sensor.temp_humidity_livingroom_humidity"))
      humidityInsideAvg = (bedroomHumidity + livingRoomHumidity) / 2
      wienHumidity = float(self.get_state("weather.temperatur_wien", attribute = "humidity"))

      plantMoisture = float(self.get_state("sensor.flora_big_livingroom_moisture"))

      self.call_service(
          "notify/CARO_WENDI_GROUP",
          title = "*Guten Morgen!*",
          message = "\n\nTemperatur:\n\t*🏠{:10.2f}°C\n\t⛅{:10.2f}°C*\n\nLuftfeuchtigkeit:\n\t*🏠{:10.2f}%\n\t⛅{:10.2f}%*\n\nFeuchtigkeit 🌿:\n\t*{:10.2f}%*".format(temperatureInsideAvg, wienTemperature, humidityInsideAvg, wienHumidity, plantMoisture)
          )