# Healthcare Expert Systems: A Heart Failure Telemonitoring Case Study

This repository demonstrates the transformative potential of rule-based expert systems in healthcare, particularly in enhancing patient self-care and improving the clinical management of heart failure. We've used Pyke, a Python-based knowledge-based system, to develop a robust and versatile tool that combines the logical expressiveness of Prolog with the wide-ranging functionality of Python.

## Health Assessment Flowchart

The flowchart below illustrates the complexity of maintaining classical expert systems. It demonstrates potential outcome states resulting from varying combinations of vital sign measurements. 

![Health Assessment Flowchart](uml/output/state-attempt-2/StateDiagram.png)

## About the Project

The project is inspired by the research of Seto et al. (2012), which focused on a rule-based expert system designed for a heart failure telemonitoring system that operates via mobile phones. The study demonstrated significant improvements in self-care and clinical management of heart failure.

This repository provides an implementation of a similar system, developed using Pyke. Pyke allows for the creation of an expert system (ES) that emulates the features of Prolog but is entirely crafted in Python.

## Pyke and Its Components

![Pyke Diagram](path-to-screenshot)

Pyke rules consist of 'if' and 'then' segments, traditionally referred to as premises and conclusions. Pyke programs contain rule bases, repositories of rules stored in .krb files. A single rule base can contain both forward-chaining and backward-chaining rules, offering flexibility in the rule execution process.

## Forward-Chaining in Pyke

Forward-chaining, the method of reasoning used in inference engines, checks if any known facts match the 'if' clause of a rule. Pyke stores these facts in .kfb files, known as fact bases.

## Analyzing the Rule Base

This repository includes several rule sets designed to monitor patient health. For instance, the rule named `high_BMI_high_BP_abnormal_HR` checks for patients who are obese, have high blood pressure, and an abnormal heart rate. If a patient meets these conditions, the system generates a message advising them to contact their doctor or visit the emergency department.

![Rule Example](path-to-screenshot)

## Running the Program

To execute the program, navigate to the directory of the driver.py file and run the command `python driver.py`. The program then outputs a domain-relevant recommendation based on the patient's vital signs, thereby enhancing the transparency of the expert system.

![Program Execution](path-to-screenshot)

## Future Development

Integrating a question rule base and back-chaining rules into the ES could significantly enhance its functionality. The ES could ask targeted questions, enabling a more comprehensive and personalized analysis of each patient's health.

## Conclusion

This project demonstrates the value of rule-based expert systems in healthcare. With continued research and development, expert systems like the one presented here can significantly improve patient care and outcomes.
