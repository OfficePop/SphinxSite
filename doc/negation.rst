============
Negation
============

Introduction
-------------

This is negation, where we negate!

+------------+------------+-----------+-----------+
| Header 1   | Header 2   | Header 3  | Header 4  |
+============+============+===========+===========+
| body row 1 | column 2   | column 3  | column 4  |
+------------+------------+-----------+-----------+
| body row 2 | Cells may span columns.| Content   |
+------------+------------+-----------+-----------+
| body row 3 | Cells may  | - Cells   | - Cells   |
+------------+ span rows. | - contain | - contain |
| body row 4 |            | - blocks. | - blocks. |
+------------+------------+-----------+-----------+

=====  =====  ======
   Inputs     Output
------------  ------
  A      B    A or B
=====  =====  ======
False  False  False
True   False  True
False  True   True
True   True   True
=====  =====  ======

 ==========   =============   ================================
 Parameter    Type            Description
 ==========   =============   ================================
 a            float/complex   coefficient for quadratic term
 b            float/complex   coefficient for linear term
 c            float/complex   coefficient for constant term
 r1, r2       float/complex   return: the two roots of
                              the quadratic polynomial
 ==========   =============   ================================
