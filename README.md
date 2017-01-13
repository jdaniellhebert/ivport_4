# ivport_4
* Work in Progress Debugging ivport_4 ( 4x camera mux for RPI - gang-able up to 16x cameras)

#### Configuration
* 6x cameras.  Board 1 fully populated.  Board 2:  camera 1 & 2 populated.
* Board 1 -- 2x A jumper bridged
* Board 1 -- XY jumpers as is, both no bridge.
* Board 2 -- 2x B jumpers
* Board 2 -- X jumper bridged.  Y jumper as is, no jumper.
* Cluster connector in place.
* Input connector to RPI camera connector tested from each board.
* Followed IVPort Setup Recipe for configuration of software.

#### Tests
 * mec_ivport_test5.py
  * Both boards connected.
  * All 4x cameras on board 1 work when Input connected to RPI from board 2.
  * All 2x cameras on board 2 work when Input connected to RPI from board 1.
 * mec_ivport_test6.py
  * Board 1 works without board 2
 *  mec_ivport_test7.py
  * Board 2 works without board 1
  
#### Status
* The multi-board configuration does not work. The analog mux signals are corrupted for the board that the input connector is on. The singals are intact on second board output connector.
* After reverse engineered schematic (see .pdf docs in repo), there do not seem to be any missing control lines that would switch between board input connectors.   
* In prinicpal mec_ivport_test5.py should work as programmed and tested. The only difference between tests is electrical hardware configuration.
* Conjecture for failure (not tested):  The difference between the two tests is electrically different because of the fanout of the second board over the cluster connector.  The signals are high speed and the line impedence is likely modified.  Other commenters have indicated that they are seeing intermittant errors.
* Next steps:  use high speed scope / logic analyzer to look at signal lines. I am not sure I will do this as there is no clear path to rework the board.

  
