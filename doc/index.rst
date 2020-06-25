====================
Endpoint: patrol
====================

The patrol endpoint provides access to all patrol reports submitted through the Vanguard Patrol App or web portal, up to the last two years. Several actions are supported by the endpoint as detailed below, and the data can be organized and filtered by multiple parameters as once (For example, data could be filtered first by date, then further by UserID or Incident).

POST https://api.vanguard.com/patrol/
=====================================

Add a patrol report. 


+------------------+-----------------------------+------------+-------------------------------------+
|  Parameter       |  Description                |     Type   |    Notes                            |
+==================+=============================+============+=====================================+
| Date             | Date the patrol             |  String    | Format is YYYY-MM-DD.               |
|                  | occurred.                   |            |                                     |
+------------------+-----------------------------+------------+-------------------------------------+
| UserID           | The alias of the individual |  String    | Matches the user’s Vanguard email   |
|                  | who submitted the patrol.   |            | alias (For example, MScott).        |
+------------------+-----------------------------+------------+-------------------------------------+
| PatrolStart      | Time the patrol started.    |  Int       | Format is 24-hour (Ex: 0700         |
|                  |                             |            | or 1400).                           |
+------------------+-----------------------------+------------+-------------------------------------+ 
| PatrolEnd        | Time the patrol ended.      |  Int       | Format is 24-hour (Ex: 0700         |
|                  |                             |            | or 1400).                           |
+------------------+-----------------------------+------------+-------------------------------------+
|PerimeterFence    |  Patrol area.               |  Object    |                                     |
+----+-------------+-----------------------------+------------+-------------------------------------+
|    |Time         | Time the area was patrolled.|  Int       | Format is 24-hour (Ex: 0700         |
|    |             |                             |            | or 1400).                           |
+----+-------------+-----------------------------+------------+-------------------------------------+
|    |Incident     | Indicates whether anything  |  Boolean   | Default value is false.             |
|    |             | unusual was encountered     |            |                                     |
|    |             | during the patrol.          |            |                                     |
+----+-------------+-----------------------------+------------+-------------------------------------+
|    |PatrolDetails| Summary of area patrol.     |  String    | When incident is false, the default |
|    |             |                             |            | value will be "Nothing to report."  |
+----+-------------+-----------------------------+------------+-------------------------------------+
|FacilityExterior  |  Patrol area.               |  Object    |                                     |
+----+-------------+-----------------------------+------------+-------------------------------------+
|    |Time         | Time the area was patrolled.|  Int       | Format is 24-hour (Ex: 0700         |
|    |             |                             |            | or 1400).                           |
+----+-------------+-----------------------------+------------+-------------------------------------+
|    |Incident     | Indicates whether anything  |  Boolean   | Default value is false.             |
|    |             | unusual was encountered     |            |                                     |
|    |             | during the patrol.          |            |                                     |
+----+-------------+-----------------------------+------------+-------------------------------------+
|    |PatrolDetails| Summary of area patrol.     |  String    | When incident is false, the default |
|    |             |                             |            | value will be "Nothing to report."  |
+----+-------------+-----------------------------+------------+-------------------------------------+
|FacilityInterior  |  Patrol area.               |  Object    |                                     |
+----+-------------+-----------------------------+------------+-------------------------------------+
|    |Time         | Time the area was patrolled.|  Int       | Format is 24-hour (Ex: 0700         |
|    |             |                             |            | or 1400).                           |
+----+-------------+-----------------------------+------------+-------------------------------------+
|    |Incident     | Indicates whether anything  |  Boolean   | Default value is false.             |
|    |             | unusual was encountered     |            |                                     |
|    |             | during the patrol.          |            |                                     |
+----+-------------+-----------------------------+------------+-------------------------------------+
|    |PatrolDetails| Summary of area patrol.     |  String    | When incident is false, the default |
|    |             |                             |            | value will be "Nothing to report."  |
+----+-------------+-----------------------------+------------+-------------------------------------+
