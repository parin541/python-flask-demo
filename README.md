Integrate SonarQube Cloud with GithubAction.

Prerequisite:
•	Already hosted project on Github and GithubAction workflow files.


Steps :
1.	Go to SonarCloud (https://sonarcloud.io) and singUp using GitHub Account. (If already have access to it, login)
2.	Click on ‘My Organization’ option from the user profile.
3.	Click on ‘Create’ and select the Github and then select your Github account.
4.	Keep the same values for ‘Name’ and ‘Key’ for Organization.
5.	Select ‘Free plan’ then click on ‘Create Organization’.
6.	Now click on ‘Analyze a new project’ button.
7.	Select project ‘Repo’ that you want form ‘SonarCloud’ Scan.
8.	Click on ‘SetUp’ and then click on ‘Previous version’ and then click ‘Create Project’.
9.	Quickly verify the default setting and create ‘myworkflow.yaml’ file for Github action.
10.	Go to root foler for project repo and add file with ‘sonar-project.properties’ and add below code also update code according to project repo name.

  sonar.organization=parin541
  sonar.projectKey=parin541_python-flask-demo
  sonar.sources=src
  sonar.python.coverage.reportPaths=coverage.xml

11.	Go to project repo in Github and add workflow file in ‘./gihub/workflow’ path for GitHub Action and add the code according to your workflow steps.
