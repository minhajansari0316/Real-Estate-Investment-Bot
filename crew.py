from crewai import Crew
from main import property_researcher
from task import property_researcher_task, analysis_task

crew = Crew(
    agents=[property_researcher],
    tasks=[property_researcher_task, analysis_task],
    verbose=True  
)

task_output = crew.kickoff()
print(task_output)

