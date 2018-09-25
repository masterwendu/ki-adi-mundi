import appdaemon.plugins.hass.hassapi as hass
import time

class CubeTVVolumeManager(hass.Hass):

  def initialize(self):
     self.listen_event(self.handleVolumeRotate, "cube_action", entity_id = "binary_sensor.cube_158d000278d378", action_type = "rotate")

  def handleVolumeRotate(self, entity, attribute, kwargs):
      actionValue = int(attribute["action_value"])
      self.log(actionValue)
      volumeScriptName = "script.tv_volume_up"
      if actionValue < 0:
          volumeScriptName = "script.tv_volume_down"
          actionValue *= -1
      for x in range(0, actionValue):
          self.turn_on(volumeScriptName)
