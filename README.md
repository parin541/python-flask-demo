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
10.	Go to root folder for project repo and add file with ‘sonar-project.properties’ and add below code also update code according to project repo name.

sonar.organization=parin541
sonar.projectKey=parin541_python-flask-demo
sonar.sources=src
sonar.python.coverage.reportPaths=coverage.xml

11.	Go to project repo in Github and add workflow file in ‘./gihub/workflow’ path for GitHub Action and add the code according to your workflow steps.

name: "sonar_cloud_scan_github_actions"
on:
  push:
    branches: [ master ]
jobs:
  DemoSonarCloudSCan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
            fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
            python-version: '3.x'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r src/requirements.txt
          pip install pytest pytest-cov
      - name: Run tests with coverage
        run: |
          pytest --cov=src --cov-report=xml
      - name: Prepare SonarCloud properties
        run: |
          echo "sonar.organization=parin541" > sonar-project.properties
          echo "sonar.projectKey=parin541_python-flask-demo" >> sonar-project.properties
          echo "sonar.sources=src" >> sonar-project.properties
          echo "sonar.python.coverage.reportPaths=coverage.xml" >> sonar-project.properties
      - name: SonarCloud Scan
        uses: SonarSource/sonarcloud-github-action@v4
        env:
            GITHUB_TOKEN: ${{ secrets.GIT_TOKEN }}
            SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}

---------------
12.	Update the ‘myworkflow.yml’ where ever it needs to be updated.
13.	Configure ‘GIT_TOKEN’ and ‘SONAR_TOKEN’ for Sonar cloud project
14.	Now create ‘SONAR_TOKEN’ from sonarqube cloud portal.
15.	Go to ‘SonarQube cloud’ 
16.	Select ‘My accounts’ >> security >> 
17.	Enter the token name ‘SONAR_TOKEN’ click on ‘Generate Token’ button
18.	Copy the token and go to project repo on github.
19.	click on ‘setting’ then click on ‘secrets and variables’ then click on ‘New repository secret’
20.	Add same name as generate for token as ‘SONAR_TOKEN’ and paste generated code in ‘Value’ and then click on ‘Add secret’ button.
21.	 Now Generate PAT token for Github.
22.	Go to Github >> Profile >>setting
23.	 Select ‘ Developer settings’
24.	Go to ‘Personal access token’  >> click on ‘Token Classic’ >> Click on ‘Generate new token’.
25.	Give note as ‘GIT_TOKEN’ >> select all the require option for scope
26.	Now click on ‘Generate Token’ and copy token value
27.	Copy the token and go to project repo on github.
28.	click on ‘setting’ then click on ‘secrets and variables’ then click ‘Actions’.
29. Add same name as generate for token as ‘GIT_TOKEN’ and paste generated code in ‘Value’ and then click on ‘Add secret’ button.
30. Now go to project code repo and push any changes in to  project repo.

