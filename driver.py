from __future__ import with_statement
import sys
from pyke import knowledge_engine
from pyke import krb_traceback
from pyke import goal

# Compile and load .krb file in same directory that I'm in (recursively).
engine = knowledge_engine.engine(__file__)

# Compiling the health goal
fc_goal = goal.compile('healthcare.message($name, $weight, $height, $systolic, $diastolic, $hr, $message)')


def fc_test():
    # Allows for running tests multiple times
    engine.reset()
    try:
        # Activating the engine - fires all FC rules
        engine.activate('fc_healthcare')
        with fc_goal.prove(engine) as gen:
            print '**************************************************************************'
            print '*                                                                        *'
            print '*   This is a test output for a Healthcare Expert System (ES) using      *'
            print '*   patient fact information from the healthcare.kfb fact base to fire   *'
            print '*   rules in the fc_healthcare.krb rule base using forward-chaining.     *'
            print '*                                                                        *'
            print '*   It generates output to the terminal that supports decision-makers    *'
            print '*   in their decision-making process.                                    *'
            print '*                                                                        *'
            print '*   This program is compatible with Python 2.6.                          *'
            print '*   You can run it by typing the following command in your terminal:     *'
            print '*                                                                        *'
            print '*   $ python driver.py                                                   *'
            print '*                                                                        *'
            print '**************************************************************************'
            for vars, plan in gen:
                # Calculating BMI
                weight_km = vars['weight'] / 2.205
                height_m = vars['height'] / 39.37
                bmi = weight_km / (height_m ** 2)
                # Obtaining Blood Pressure (BP)
                bp = str(vars['systolic']) + '/' + str(vars['diastolic'])
                # Outputting Results
                print "\n   Patient Name: %s" % (vars['name'])
                print "------------------------------------"
                print "    Weight (lbs): %s" % (vars['weight'])
                print "    Height (inch): %s" % (vars['height'])
                print "    Body Mass Index (BMI): %.2f" % bmi
                print "    Blood Pressure (BP): %s" % (bp)
                print "    Heart Rate (HR): %s" % (vars['hr'])
                print "    %s" % (vars['message'])
                print "------------------------------------\n"
    except:
        krb_traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    fc_test()
