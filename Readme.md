## SonarQube Python Code Coverage

### Prerequisites

1. Set up a local or cloud instance of the [SonarQube server](https://docs.sonarsource.com/sonarqube-server/10.8/try-out-sonarqube/). Create a project using the SonarQube dashboard and generate a [project analysis token](https://docs.sonarsource.com/sonarqube-server/latest/user-guide/managing-tokens/).
2. Install Python 3.7 or above. 

### Install Python dependencies

Install python application dependencies using `pip`.

```
pip install -r requirements.txt
```

### Generate code coverage

Execute the following commands in the terminal to generate an XML code coverage report.

```
coverage run -m pytest
coverage xml
```

### Run analysis

```
pysonar-scanner -Dsonar.token=<YOUR_SONARQUBE_PROJECT_TOKEN>
```

Note: Replace `<YOUR_SONARQUBE_PROJECT_TOKEN>` with your SonarQube Project token. 

Once the report is generated, head over to the SonarQube dashboard to review the results. 
