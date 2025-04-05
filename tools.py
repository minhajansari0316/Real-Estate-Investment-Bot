
import os
from crewai_tools import SerperDevTool



os.environ["Serper_Dev_tool"] = "ea9896b330b947e239a45697b0cd12486fe12843"
Serper_Dev_tool = os.environ["Serper_Dev_tool"]

search_tool = SerperDevTool()