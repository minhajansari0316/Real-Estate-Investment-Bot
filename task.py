from crewai import Task
from main import property_researcher, property_analyst

property_researcher_task = Task(
    description="""Conduct a comprehensive analysis of potential retail property investments in the specified market.

    Specific research requirements:
    1. Market Analysis:
       - Identify top 3-5 potential retail property investment locations
       - Analyze current market trends and economic indicators
       - Assess demographic data and consumer spending patterns
       - Evaluate local retail ecosystem and potential tenant mix

    2. Property Evaluation Criteria:
       - Foot traffic analysis
       - Accessibility and transportation infrastructure
       - Proximity to complementary businesses
       - Local economic development plans

    3. Financial Analysis:
       - Estimate potential rental yields
       - Calculate projected ROI
       - Assess property valuation and appreciation potential
       - Identify potential renovation or repositioning opportunities

    4. Risk Assessment:
       - Analyze competitor landscape
       - Evaluate e-commerce impact on local retail
       - Assess potential regulatory or zoning challenges
       - Identify potential long-term growth barriers

    5. Detailed Reporting:
       Provide a comprehensive report with:
         - Executive summary
         - Detailed market insights
         - Property recommendations
         - Financial projections
         - Risk analysis
         - Visual aids (charts, graphs)

    Deliverable: A comprehensive, data-driven investment recommendation report.""",

    expected_output="""Detailed report containing:
    - Market analysis summary
    - Top 3-5 recommended retail property investments
    - Comprehensive financial projections
    - Risk assessment
    - Recommendations for further due diligence""",

    agent=property_researcher,
    output_file="research_taskoutput.txt"
)

analysis_task = Task(
    description="Summarise the property information into bullet point list. ",
    expected_output="A summarised dot point list of each of the suburbs, prices and important features of that suburb.",
    agent=property_analyst,
    output_file="task2_output.txt",
)
