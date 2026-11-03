\# IT3180 - AIMS Project Report



\## 1. Project Overview



AIMS (An Internet-based Advanced Management System) is a simple DVD management application developed using Python.



The project demonstrates basic software development and Git/GitHub version control practices.



\## 2. Main Features



\- Display the available DVD list.

\- Add DVDs to a shopping cart.

\- Display shopping cart information.

\- Search DVDs by title.

\- Calculate the total price.

\- Apply discounts based on the number of DVDs purchased.



\## 3. Technologies Used



\- Python 3

\- Git

\- GitHub

\- GitHub Actions

\- Python unittest



\## 4. Project Structure



```text

IT3180-AIMS/

├── .github/

│   └── workflows/

│       └── python-tests.yml

├── aims/

│   └── main.py

├── docs/

│   └── PROJECT\_REPORT.md

├── tests/

│   └── test\_aims.py

├── .gitignore

├── CHANGELOG.md

└── README.md

```



\## 5. Git and GitHub Practices



The following practices were performed during development:



1\. Initialize a Git repository and connect it to GitHub.

2\. Create commits to record project changes.

3\. Create feature branches for new functionality.

4\. Create and merge Pull Requests.

5\. Resolve merge conflicts.

6\. Use `git revert` to undo changes while preserving commit history.

7\. Create version tags and publish a GitHub Release.

8\. Create a hotfix branch to update application data.

9\. Practice `git cherry-pick` to apply a specific commit.

10\. Configure GitHub Actions to automatically run unit tests.



\## 6. Testing



The project uses Python's built-in `unittest` framework.



Run tests using:



```bash

py -m unittest discover -s tests -v

```



The current test cases cover:



\- DVD object creation.

\- Initial DVD list.

\- Adding a DVD to the shopping cart.



\## 7. Continuous Integration



GitHub Actions is configured to run unit tests automatically when code is pushed to the `main` branch or when a Pull Request targets `main`.



\## 8. Conclusion



This project provides practical experience in Python application development and Git/GitHub workflows, including version control, collaboration through Pull Requests, release management, and automated testing.



\## 9. Author



Nguyen Hoang Oanh

