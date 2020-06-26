====================
Endpoint: patrol
====================

The patrol endpoint provides access to all patrol reports submitted through the Vanguard Patrol App or web portal, up to the last two years. Several actions are supported by the endpoint, as detailed below.

.. toctree::
   :caption: Actions
   
   index
    
Submit a patrol
=====================================

URL: POST https://api.vanguard.com/patrol/{PatrolID}

Adds a patrol report. A successful response requires all listed parameters be included with appropriate values.

+------------------+-----------------------------+------------+-------------------------------------+
|  Parameter       |  Description                |  Type      |    Notes                            |
+==================+=============================+============+=====================================+
| patrolID         | ID of the submitted patrol. |  int       | Assigned automatically by the patrol|
|                  |                             |            | app.                                |
+------------------+-----------------------------+------------+-------------------------------------+
| date             | Date the patrol             |  string    | Format is YYYY-MM-DD.               |
|                  | occurred.                   |            |                                     |
+------------------+-----------------------------+------------+-------------------------------------+
| userID           | The alias of the individual |  string    | Matches the user’s Vanguard email   |
|                  | who submitted the patrol.   |            | alias (For example, MScott).        |
+------------------+-----------------------------+------------+-------------------------------------+
| patrolStart      | Time the patrol started.    |  int       | Format is 24-hour (Ex: 0700         |
|                  |                             |            | or 1400).                           |
+------------------+-----------------------------+------------+-------------------------------------+ 
| patrolEnd        | Time the patrol ended.      |  int       | Format is 24-hour (Ex: 0700         |
|                  |                             |            | or 1400).                           |
+------------------+-----------------------------+------------+-------------------------------------+
|perimeterFence    |  Patrol area.               |  object    |                                     |
+----+-------------+-----------------------------+------------+-------------------------------------+
|    |time         | Time the area was patrolled.|  int       | Format is 24-hour (Ex: 0700         |
|    |             |                             |            | or 1400).                           |
+----+-------------+-----------------------------+------------+-------------------------------------+
|    |incident     | Indicates whether anything  |  boolean   | Default value is false.             |
|    |             | unusual was encountered     |            |                                     |
|    |             | during the patrol.          |            |                                     |
+----+-------------+-----------------------------+------------+-------------------------------------+
|    |details      | Summary of area patrol.     |  string    | When incident is false, the default |
|    |             |                             |            | value will be "Nothing to report."  |
+----+-------------+-----------------------------+------------+-------------------------------------+
|facilityExterior  |  Patrol area.               |  object    |                                     |
+----+-------------+-----------------------------+------------+-------------------------------------+
|    |time         | Time the area was patrolled.|  int       | Format is 24-hour (Ex: 0700         |
|    |             |                             |            | or 1400).                           |
+----+-------------+-----------------------------+------------+-------------------------------------+
|    |incident     | Indicates whether anything  |  boolean   | Default value is false.             |
|    |             | unusual was encountered     |            |                                     |
|    |             | during the patrol.          |            |                                     |
+----+-------------+-----------------------------+------------+-------------------------------------+
|    |details      | Summary of area patrol.     |  string    | When incident is false, the default |
|    |             |                             |            | value will be "Nothing to report."  |
+----+-------------+-----------------------------+------------+-------------------------------------+
|facilityInterior  |  Patrol area.               |  object    |                                     |
+----+-------------+-----------------------------+------------+-------------------------------------+
|    |time         | Time the area was patrolled.|  int       | Format is 24-hour (Ex: 0700         |
|    |             |                             |            | or 1400).                           |
+----+-------------+-----------------------------+------------+-------------------------------------+
|    |incident     | Indicates whether anything  |  boolean   | Default value is false.             |
|    |             | unusual was encountered     |            |                                     |
|    |             | during the patrol.          |            |                                     |
+----+-------------+-----------------------------+------------+-------------------------------------+
|    |details      | Summary of area patrol.     |  string    | When incident is false, the default |
|    |             |                             |            | value will be "Nothing to report."  |
+----+-------------+-----------------------------+------------+-------------------------------------+

**Responses**

========= ================
 **Code**  **Description** 
--------- ----------------
 200       Successful operation.
========= ================

:: 
   
   {
     "patrolId": 789654,
     "userId": "MDavid",
     "date": "2020-04-18",
     "patrolStart": 0700,
     "patrolEnd": 0800,
     "perimeterFence":{
      "time": 0700,
      "incident": false,
      "details": "Nothing to report."
     },
     "facilityExterior":{
       "yime": 0733,
       "incident": false,
       "details": "Nothing to report."
     },
     "facilityInterior":{
       "time": 0749,
       "incident": true,
       "details": "At approximately 0755, Encountered an open fire escape in western corridor. Notified dispatcher, closed fire escape, and queried 
       individuals in the area. Fire escape had been opened and de-alarmed for maintenance but was not properly closed."
     }
   }
   
========= ================
 **Code**  **Description** 
--------- ----------------
 400       Invalid or missing input.
========= ================

Find a patrol report
=====================================

URL: GET https://api.vanguard.com/patrol/{PatrolID/Date/UserID}

List a patrol report. At least one instance of the patrolID, date, or userID parameter is required. Queries can be run with several parameters to further 
refine data.

+------------------+-----------------------------+------------+-------------------------------------+
|  Parameter       |  Description                |     Type   |    Notes                            |
+==================+=============================+============+=====================================+
| patrolID         | ID of the submitted patrol. |  int       | Assigned automatically by the patrol|
|                  |                             |            | app.                                |
+------------------+-----------------------------+------------+-------------------------------------+
| date             | Date the patrol             |  string    | Format is YYYY-MM-DD.               |
|                  | occurred.                   |            |                                     |
+------------------+-----------------------------+------------+-------------------------------------+
| userID           | The alias of the individual |  string    | Matches the user’s Vanguard email   |
|                  | who submitted the patrol.   |            | alias (For example, MScott).        |
+------------------+-----------------------------+------------+-------------------------------------+
| incident         | Indicates whether anything  |  boolean   | "True" will display any reports     |
|                  | unusual was encountered     |            | where the patrol officer witnessed  |
|                  | during the patrol.          |            | an incident in at least one area.   |
+------------------+-----------------------------+------------+-------------------------------------+

**Query Examples**

==========================================================   ============================================================
**Usage**                                                    **URL**
----------------------------------------------------------   ------------------------------------------------------------
Find a specific patrol by ID.                                https://api.vanguard.com/patrol?patrolID=546387
Find all patrols for a given date.                           https://api.vanguard.com/patrol?date=20200517
Find all patrols on a given date that had incidents.         https://api.vanguard.com/patrol?date=20200517&incident=true
Find all patrols by a specific individual on a given date.   https://api.vanguard.com/patrol?UserID=MDavid&date=20200517
==========================================================   ============================================================

**Responses**

========= ================
 **Code**  **Description** 
--------- ----------------
 200       Successful operation.
========= ================

::

  {
    "patrolId": 546387,
    "userId": "MDavid",
    "date": "2020-05-17",
    "patrolStart": 1000,
    "patrolEnd": 1100,
    "perimeterFence":{
      "time": 1000,
      "incident": false,
      "details": "Nothing to report."
    },
    "facilityExterior":{
      "time": 1024,
      "incident": false,
      "details": "Nothing to report."
    },
    "facilityInterior":{
      "time": 1049,
      "incident": false,
      "details": "Nothing to report."
    }
  }

========= ================
 **Code**  **Description** 
--------- ----------------
 400       Invalid or missing input.
 404       Patrol not found.
========= ================

Modify a patrol report
=====================================

URL: PUT https://api.vanguard.com/patrol/{PatrolID}

Updates a submitted patrol report with new or additional data. patrolID parameter is required.

============== =========================== ======== ==========================================
 **Parameter**  **Description**            **Type** **Notes**
-------------- --------------------------- -------- ------------------------------------------
 patrolID      ID of the submitted patrol.   Int     Assigned automatically by the patrol app.
============== =========================== ======== ==========================================

**Responses**

========= ================
 **Code**  **Description** 
--------- ----------------
 200       Successful operation.
 400       Invalid or missing input.
 404       Patrol not found.
========= ================

Delete a patrol
=======================================

URL: DELETE https://api.vanguard.com/patrol/{patrolID}

Deletes a patrol report. PatrolID parameter is required. As a measure of Data Loss Prevention, deleted patrol reports are first archived in a separate 
database for 30 days before they are permanently deleted.

============== =========================== ======== ==========================================
 **Parameter**  **Description**            **Type** **Notes**
-------------- --------------------------- -------- ------------------------------------------
 patrolID      ID of the submitted patrol.   Int     Assigned automatically by the patrol app.
============== =========================== ======== ==========================================

**Responses**

========= ================
 **Code**  **Description** 
--------- ----------------
 200       Successful operation.
 400       Invalid or missing input.
 404       Patrol not found.
========= ================

