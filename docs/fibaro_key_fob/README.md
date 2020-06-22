# Fibaro keyfob remote control
* [Fibaro FIBEFGKF-601 KeyFob](https://www.amazon.de/Fibaro-FIBEFGKF-601-KeyFob-SmartHome-Fernbedienung-Wei%C3%9F/dp/B01N193MHH/ref=sr_1_1?ie=UTF8&qid=1521282386&sr=8-1&keywords=fibaro+keyfob)

## Installation
* Include it to your z-wave network via the z-wave config panel in home assistant
* shutdown homeassistant
* in your home assistant config open the file zwcfg_*.xml (the * is some hex number like `0xf55525e8`)
* search for the number of your connected remote node
  * my remote has number 6 so I found this tag: `<Node id="6" name="Remote" location="" basic="4" generic="24" specific="1" roletype="4" devicetype="5632" nodetype="0" type="Basic Wall Controller" listening="false" frequentListening="false" beaming="true" routing="true" max_baud_rate="40000" version="4" query_stage="Complete">`
* in this node tag search for `<CommandClass id="91" name="COMMAND_CLASS_CENTRAL_SCENE" version="1" request_flags="4" innif="true" scenecount="0">`
* now replace the content of this tag with:
```
<Instance index="1" />
<Value type="int" genre="system" instance="1" index="0" units="" read_only="true" write_only="false" verify_changes="false" poll_intensity="0" min="-2147483648" max="2147483647" value="6" label="Scene Count" />
<Value type="int" genre="user" instance="1" index="1" units="" read_only="false" write_only="false" verify_changes="false" poll_intensity="0" min="-2147483648" max="2147483647" value="0" label="Square" />
<Value type="int" genre="user" instance="1" index="2" units="" read_only="false" write_only="false" verify_changes="false" poll_intensity="0" min="-2147483648" max="2147483647" value="0" label="Circle" />
<Value type="int" genre="user" instance="1" index="3" units="" read_only="false" write_only="false" verify_changes="false" poll_intensity="0" min="-2147483648" max="2147483647" value="0" label="X" />
<Value type="int" genre="user" instance="1" index="4" units="" read_only="false" write_only="false" verify_changes="false" poll_intensity="0" min="-2147483648" max="2147483647" value="0" label="Triangle" />
<Value type="int" genre="user" instance="1" index="5" units="" read_only="false" write_only="false" verify_changes="false" poll_intensity="0" min="-2147483648" max="2147483647" value="0" label="Minus" />
<Value type="int" genre="user" instance="1" index="6" units="" read_only="false" write_only="false" verify_changes="false" poll_intensity="0" min="-2147483648" max="2147483647" value="0" label="Plus" />
<Value type="int" genre="user" instance="1" index="7" units="" read_only="false" write_only="false" verify_changes="false" poll_intensity="0" min="-2147483648" max="2147483647" value="0" label="Scene 1" />
<Value type="int" genre="user" instance="1" index="8" units="" read_only="false" write_only="false" verify_changes="false" poll_intensity="0" min="-2147483648" max="2147483647" value="0" label="Scene 2" />
<Value type="int" genre="user" instance="1" index="9" units="" read_only="false" write_only="false" verify_changes="false" poll_intensity="0" min="-2147483648" max="2147483647" value="0" label="Scene 3" />
<Value type="int" genre="user" instance="1" index="10" units="" read_only="false" write_only="false" verify_changes="false" poll_intensity="0" min="-2147483648" max="2147483647" value="0" label="Scene 4" />
<Value type="int" genre="user" instance="1" index="11" units="" read_only="false" write_only="false" verify_changes="false" poll_intensity="0" min="-2147483648" max="2147483647" value="0" label="Scene 5" />
<Value type="int" genre="user" instance="1" index="12" units="" read_only="false" write_only="false" verify_changes="false" poll_intensity="0" min="-2147483648" max="2147483647" value="0" label="Scene 6" />
```
* and start your home assistant again.
* now home assistant can handle the scenes of the remote
* in the z-wave control panel you can now activate the buttons as you like (single press, long press....)
* take a look at the OZW Log to know the scene values
  * for example this is a log when pression on the plus key
  ```
      2018-03-17 11:34:47.962 Info, Node006, Received Central Scene set from node 6: scene id=6 in 7680 seconds. Sending event notification.
      2018-03-17 11:34:47.962 Detail, Node006, Refreshed Value: old value=7680, new value=7680, type=int
  ```
  * id is the id of the scene
  * and the seconds are no secends this is the scene_data (this says if it's a single, double press...), I have no idea why it's the seconds value but it works :)
* Take a look into my `configuration/automation/keyFobRemote.yaml` file to see how to handle scenes

### full example of the CommandClass tag:
```
<CommandClass id="91" name="COMMAND_CLASS_CENTRAL_SCENE" version="1" request_flags="4" innif="true" scenecount="0">
    <Instance index="1" />
    <Value type="int" genre="system" instance="1" index="0" units="" read_only="true" write_only="false" verify_changes="false" poll_intensity="0" min="-2147483648" max="2147483647" value="6" label="Scene Count" />
    <Value type="int" genre="user" instance="1" index="1" units="" read_only="false" write_only="false" verify_changes="false" poll_intensity="0" min="-2147483648" max="2147483647" value="0" label="Square" />
    <Value type="int" genre="user" instance="1" index="2" units="" read_only="false" write_only="false" verify_changes="false" poll_intensity="0" min="-2147483648" max="2147483647" value="0" label="Circle" />
    <Value type="int" genre="user" instance="1" index="3" units="" read_only="false" write_only="false" verify_changes="false" poll_intensity="0" min="-2147483648" max="2147483647" value="0" label="X" />
    <Value type="int" genre="user" instance="1" index="4" units="" read_only="false" write_only="false" verify_changes="false" poll_intensity="0" min="-2147483648" max="2147483647" value="0" label="Triangle" />
    <Value type="int" genre="user" instance="1" index="5" units="" read_only="false" write_only="false" verify_changes="false" poll_intensity="0" min="-2147483648" max="2147483647" value="0" label="Minus" />
    <Value type="int" genre="user" instance="1" index="6" units="" read_only="false" write_only="false" verify_changes="false" poll_intensity="0" min="-2147483648" max="2147483647" value="0" label="Plus" />
    <Value type="int" genre="user" instance="1" index="7" units="" read_only="false" write_only="false" verify_changes="false" poll_intensity="0" min="-2147483648" max="2147483647" value="0" label="Scene 1" />
    <Value type="int" genre="user" instance="1" index="8" units="" read_only="false" write_only="false" verify_changes="false" poll_intensity="0" min="-2147483648" max="2147483647" value="0" label="Scene 2" />
    <Value type="int" genre="user" instance="1" index="9" units="" read_only="false" write_only="false" verify_changes="false" poll_intensity="0" min="-2147483648" max="2147483647" value="0" label="Scene 3" />
    <Value type="int" genre="user" instance="1" index="10" units="" read_only="false" write_only="false" verify_changes="false" poll_intensity="0" min="-2147483648" max="2147483647" value="0" label="Scene 4" />
    <Value type="int" genre="user" instance="1" index="11" units="" read_only="false" write_only="false" verify_changes="false" poll_intensity="0" min="-2147483648" max="2147483647" value="0" label="Scene 5" />
    <Value type="int" genre="user" instance="1" index="12" units="" read_only="false" write_only="false" verify_changes="false" poll_intensity="0" min="-2147483648" max="2147483647" value="0" label="Scene 6" />
</CommandClass>
```