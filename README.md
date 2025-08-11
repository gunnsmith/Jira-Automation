# Jira-Automation

Python script for automating the creation of tickets in Jira with "boilerplate text".
(including WYSIWYG styles)

## Setup

At the top of the file, fill in the below fields in order for the script to connect to your
Jira instance and create the tickets in the desired project.

User Info:
API_KEY - this can be generated from your user account settings, under the Security tab.
JIRA_EMAIL - this should be the email address used for the user account tied to the api key above.

Jira Instance Info:
BASE_URL - atlassian url for your Jira instance.
PROJECT_KEY - key of the project that you want the tickets created under. Found in your project's settings.

## Usage

The below flags can be used when running the script from the terminal.

Required Flag:

-t OR --topic
Used for supplying the topic of the ticket that will be created. Any text that is
wrapped in quotes after this flag will be added to the summary of the ticket.

Optional Flags for changing ticket type:

-s OR --story
Set to true by default. Includes user statement, user types, and starter Acceptance Criteria list.

-b OR --bug
Overrides the story flag. Includes reproduction steps list, issue list, and expected list.

-d OR --defect
Overrides the story flag. Includes reproduction steps list, issue list, and expected list.
