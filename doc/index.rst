====================
Endpoint: patrol
====================

The patrol endpoint provides access to all patrol reports submitted through the Vanguard Patrol App or web portal, up to the last two years. Several actions are supported by the endpoint as detailed below, and the data can be organized and filtered by multiple parameters as once (For example, data could be filtered first by date, then further by UserID or Incident).

+------------------+-----------------------------+------------+-------------------------------------+
|  Parameter       |  Description                |     Type   |    Notes                            |
+==================+=============================+============+=====================================+
| PatrolID         | ID of the submitted patrol. |  Int       | Assigned automatically by the patrol|
|                  |                             |            | app.                                |
+------------------+-----------------------------+------------+-------------------------------------+
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
|    |Details      | Summary of area patrol.     |  String    | When incident is false, the default |
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
|    |Details      | Summary of area patrol.     |  String    | When incident is false, the default |
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
|    |Details      | Summary of area patrol.     |  String    | When incident is false, the default |
|    |             |                             |            | value will be "Nothing to report."  |
+----+-------------+-----------------------------+------------+-------------------------------------+

POST https://api.vanguard.com/patrol/
=====================================

Adds a patrol report. A successful response requires all listed parameters be included with appropriate values.

**Responses**

========= ================
 **Code**  **Description** 
--------- ----------------
 200       Successful operation.
========= ================

.. code-block:: json
   
   {
     "patrolId": 789654,
     "userId": "MDavid",
     "Date": "2020-04-18",
     "PatrolStart": 0700,
     "PatrolEnd": 0800,
     "PerimeterFence":{
      "Time": 0700,
      "Incident": false,
      "PatrolDetails": "Nothing to report."
     },
     "FacilityExterior":{
       "Time": 0733,
       "Incident": false,
       "PatrolDetails": "Nothing to report."
     },
     "FacilityInterior":{
       "Time": 0749,
       "Incident": true,
       "PatrolDetails": "At approximately 0755, Encountered an open fire escape in western corridor. Notified dispatcher, closed fire escape, and queried individuals in the 
       area. Fire escape had been opened and de-alarmed for maintenance but was not properly closed."
     }
   }
   
========= ================
 **Code**  **Description** 
--------- ----------------
 400       Invalid or missing input.
========= ================

GET https://api.vanguard.com/patrol/{patrolID}
=====================================

List a patrol report.

+------------------+-----------------------------+------------+-------------------------------------+
|  Parameter       |  Description                |     Type   |    Notes                            |
+==================+=============================+============+=====================================+
| PatrolID         | ID of the submitted patrol. |  Int       | Assigned automatically by the patrol|
|                  |                             |            | app.                                |
+------------------+-----------------------------+------------+-------------------------------------+
| Date             | Date the patrol             |  String    | Format is YYYY-MM-DD.               |
|                  | occurred.                   |            |                                     |
+------------------+-----------------------------+------------+-------------------------------------+
| UserID           | The alias of the individual |  String    | Matches the user’s Vanguard email   |
|                  | who submitted the patrol.   |            | alias (For example, MScott).        |
+------------------+-----------------------------+------------+-------------------------------------+
| Incident         | Indicates whether anything  |  Boolean   | "True" will display any reports     |
|                  | unusual was encountered     |            | where the patrol officer witnessed |
|                  | during the patrol.          |            | an incident in at least one area.  |
+------------------+-----------------------------+------------+-------------------------------------+

**Query Examples**

==========================================================   ============================================================
**Usage**                                                    **URL**
----------------------------------------------------------   ------------------------------------------------------------
Find a specific patrol by ID.                                https://api.vanguard.com/patrol?patrolID=54638
Find all patrols for a given date.                           https://api.vanguard.com/patrol?date=20200517
Find all patrols on a given date that had incidents.         https://api.vanguard.com/patrol?date=20200517&incident=true
Find all patrols by a specific individual on a given date.   https://api.vanguard.com/patrol?UserID=MDavis&date=20200517
==========================================================   ============================================================
