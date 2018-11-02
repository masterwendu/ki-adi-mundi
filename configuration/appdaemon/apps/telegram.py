import appdaemon.plugins.hass.hassapi as hass
import time

class TelegramNotificationManager(hass.Hass):

  def initialize(self):
    time = datetime.time(7, 00, 0)
    self.run_daily(self.sendDailyNotification, time)

    self.listen_event(self.sendDailyNotification, "telegram_command", command = "/status")
    self.listen_event(self.sendDailyNotification, "telegram_callback", command = "/status")

  def sendDailyNotification(self, kwargs):
      bedroomTemperature = self.get_state("sensor.temp_humidity_bedroom_temperature")
      livingRoomTemperature = self.get_state("sensor.temp_humidity_livingroom_temperature")
      temperatureInsideAvg = (bedroomTemperature + livingRoomTemperature) / 2
      wienTemperature = self.get_state("weather.temperatur_wien", "temperature")

      bedroomHumidity = self.get_state("sensor.temp_humidity_bedroom_humidity")
      livingRoomHumidity = self.get_state("sensor.temp_humidity_livingroom_humidity")
      humidityInsideAvg = (bedroomHumidity + livingRoomHumidity) / 2
      wienHumidity = self.get_state("weather.temperatur_wien", "humidity")

      plantMoisture = self.get_state("sensor.flora_big_livingroom_moisture")

      self.call_service(
          "notify/CARO_WENDI_GROUP",
          title = "*Guten Morgen Caro und Wendi!*",
          message = "Temperatur (Innen / Außen): *{} / {} °C*, Luftfeuchtigkeit (Innen / Außen): *{} / {} %*, Feuchtigkeit der Pflanze: *{} %*".format(temperatureInsideAvg, wienTemperature, humidityInsideAvg, wienHumidity, plantMoisture)
          )