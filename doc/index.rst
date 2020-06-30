====================
Endpoint: patrol
====================

The patrol endpoint provides access to all patrol reports submitted through the Vanguard Patrol App or web portal, up to the last two years. Several actions are supported by the endpoint, as detailed below.

Also available in Swagger_.

.. _Swagger: https://app.swaggerhub.com/apis-docs/MDezProjects/vanguard-api/0.1.9

.. contents:: Actions
   :local:
    
Submit a patrol
=====================================

.. http:post:: https://api.vanguard.com/patrol/

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


+------+-----------------------+
| Code |  Description          |               
+======+=======================+
| 200  | Successful operation. |         
+------+-----------------------+

**JSON Body**
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
       "time": 0733,
       "incident": false,
       "details": "Nothing to report."
     },
     "facilityInterior":{
       "time": 0749,
       "incident": true,
       "details": "Found entry door propped open at approximately 0755."
     }
   }

+------+---------------------------+
| Code |  Description              |               
+======+===========================+
| 400  | Invalid or missing input. |         
+------+---------------------------+

Find a patrol report
=====================================

.. http:get:: https://api.vanguard.com/patrol/{PatrolID}
.. http:get:: https://api.vanguard.com/patrol/{Date}
.. http:get:: https://api.vanguard.com/patrol/{UserID}

    List a patrol report. Each request requires at least one query parameter, and can add more to further refine data. 

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

+----------------------------------------------------------+-------------------------------------------------------------+
| Usage                                                    |  URL                                                        |                
+==========================================================+=============================================================+
|Find a specific patrol by ID.                             |  https://api.vanguard.com/patrol?patrolID=546387            |
+----------------------------------------------------------+-------------------------------------------------------------+
|Find all patrols for a given date.                        |  https://api.vanguard.com/patrol?date=20200517              |
+----------------------------------------------------------+-------------------------------------------------------------+
|Find all patrols on a given date that had incidents.      |  https://api.vanguard.com/patrol?date=20200517&incident=true|
+----------------------------------------------------------+-------------------------------------------------------------+
|Find all patrols by a specific individual on a given date.|  https://api.vanguard.com/patrol?UserID=MDavid&date=20200517|
+----------------------------------------------------------+-------------------------------------------------------------+

**Responses**

+------+-----------------------+
| Code |  Description          |               
+======+=======================+
| 200  | Successful operation. |         
+------+-----------------------+

**JSON Body**
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

+------+---------------------------+
| Code |  Description              |               
+======+===========================+
| 400  | Invalid or missing input. |
+------+---------------------------+
| 404  | Patrol not found.         |
+------+---------------------------+

Modify a patrol report
=====================================

.. http:put:: https://api.vanguard.com/patrol/{PatrolID}

    Updates a submitted patrol report with new or additional data. patrolID parameter is required.

+------------------+-----------------------------+------------+-------------------------------------+
|  Parameter       |  Description                |     Type   |    Notes                            |
+==================+=============================+============+=====================================+
| patrolID         | ID of the submitted patrol. |  int       | Assigned automatically by the patrol|
|                  |                             |            | app.                                |
+------------------+-----------------------------+------------+-------------------------------------+

**Responses**

+------+---------------------------+
| Code |  Description              |               
+======+===========================+
| 200  | Successful operation.     |
+------+---------------------------+
| 400  | Invalid or missing input. |
+------+---------------------------+
| 404  | Patrol not found.         |
+------+---------------------------+

Delete a patrol
=======================================

.. http:delete:: https://api.vanguard.com/patrol/{patrolID}

    Deletes a patrol report. PatrolID parameter is required. As a measure of Data Loss Prevention, deleted patrol reports are first archived in a separate database for 30 days 
    before they are permanently deleted.

+------------------+-----------------------------+------------+-------------------------------------+
|  Parameter       |  Description                |     Type   |    Notes                            |
+==================+=============================+============+=====================================+
| patrolID         | ID of the submitted patrol. |  int       | Assigned automatically by the patrol|
|                  |                             |            | app.                                |
+------------------+-----------------------------+------------+-------------------------------------+

**Responses**

+------+---------------------------+
| Code |  Description              |               
+======+===========================+
| 200  | Successful operation.     |
+------+---------------------------+
| 400  | Invalid or missing input. |
+------+---------------------------+
| 404  | Patrol not found.         |
+------+---------------------------+
