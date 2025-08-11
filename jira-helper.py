import argparse
import json
import requests

# User Profile info from Jira
API_KEY = ''
JIRA_EMAIL = ''

# Jira environment info
BASE_URL = ''
PROJECT_KEY = ''

AUTH = requests.auth.HTTPBasicAuth(JIRA_EMAIL, API_KEY)
HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}


# Parse command line arguments
parser = argparse.ArgumentParser(
    prog='Jira Helper',
    description='When configured correctly, this script assists in writing boilerplate text for Jira tickets and creates them in the backlog.'
)

parser.add_argument(
    "-s", "--story", action="store_true", default=True, required=False,
    help="Used to create a Story ticket in Jira. Defaults to true if omitted."
)

parser.add_argument(
    "-b", "--bug", action="store_true", default=False, required=False,
    help="Used to create a Bug ticket in Jira. Defaults to false if omitted."
)

parser.add_argument(
    "-d", "--defect", action="store_true", default=False, required=False,
    help="Used to create a Defect ticket in Jira. Defaults to false if omitted."
)

parser.add_argument(
    "-t", "--topic", required=True,
    help="Include a topic for your ticket wrapped in quotes. Example: -t 'My topic'."
)

args = parser.parse_args()


def main():
    topic = args.topic
    issue = 'Story'

    if args.bug == True:
        issue = 'Bug'
    elif args.defect == True:
        issue = 'Defect'

    # build description text & create ticket in Jira
    desc = build_desc(topic, issue)
    res = create_ticket(
        summary=f"Placeholder - {topic}", project=PROJECT_KEY, description=desc, issue_type=issue, priority='Medium'
    )
    # print error messages in terminal if request fails
    if res.status_code == 400:
        json_res = json.loads(res.text)
        print(f"Error: {json_res['errors']}")
    else:
        json_res = json.loads(res.text)
        ticket_key = json_res['key']
        # Display link to ticket in terminal after creation
        print(f"Link: {BASE_URL}/browse/{ticket_key}")


# Create the description text as Atlassian Document Format (ADF) with WYSIWYG styles
# Generated in Atlassian's ADF Builder: https://developer.atlassian.com/cloud/jira/platform/apis/document/playground/
def build_desc(topic, issue):
    if issue == 'Story':
        description = {
            "version": 1,
            "type": "doc",
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": f"As a User, I need . . . {topic} . . ."
                        }
                    ]
                },
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "Note: "
                        },
                        {
                            "type": "text",
                            "text": "User in AC is District Admin, Building Admin, Staff User, District Volunteer Coordinator, Building Volunteer Coordinator, and Internal Super User.",
                            "marks": [
                                {
                                    "type": "em"
                                }
                            ]
                        }
                    ]
                },
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "Acceptance Criteria:",
                            "marks": [
                                {
                                    "type": "strong"
                                }
                            ]
                        }
                    ]
                },
                {
                    "type": "orderedList",
                    "attrs": {
                        "order": 1
                    },
                    "content": [
                        {
                            "type": "listItem",
                            "content": [
                                {
                                    "type": "paragraph",
                                    "content": [
                                        {
                                            "type": "text",
                                            "text": "User will navigate to . . ."
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "listItem",
                            "content": [
                                {
                                    "type": "paragraph",
                                    "content": [
                                        {
                                            "type": "text",
                                            "text": "then . . ."
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "listItem",
                            "content": [
                                {
                                    "type": "paragraph",
                                    "content": [
                                        {
                                            "type": "text",
                                            "text": "and then . . ."
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    elif (issue == 'Bug') or (issue == 'Defect'):
        description = {
            "version": 1,
            "type": "doc",
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "Steps to Reproduce:",
                            "marks": [
                                {
                                    "type": "strong"
                                }
                            ]
                        }
                    ]
                },
                {
                    "type": "orderedList",
                    "attrs": {
                        "order": 1
                    },
                    "content": [
                        {
                            "type": "listItem",
                            "content": [
                                {
                                    "type": "paragraph",
                                    "content": [
                                        {
                                            "type": "text",
                                            "text": "Navigate to . . ."
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "listItem",
                            "content": [
                                {
                                    "type": "paragraph",
                                    "content": [
                                        {
                                            "type": "text",
                                            "text": "then . . ."
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "listItem",
                            "content": [
                                {
                                    "type": "paragraph",
                                    "content": [
                                        {
                                            "type": "text",
                                            "text": "and then . . ."
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "Current Functionality:",
                            "marks": [
                                {
                                    "type": "strong"
                                },
                                {
                                    "type": "textColor",
                                    "attrs": {
                                            "color": "#ff5630"
                                    }
                                }
                            ]
                        }
                    ]
                },
                {
                    "type": "orderedList",
                    "attrs": {
                        "order": 1
                    },
                    "content": [
                        {
                            "type": "listItem",
                            "content": [
                                {
                                    "type": "paragraph",
                                    "content": [
                                        {
                                            "type": "text",
                                            "text": ". . ."
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "Expected Functionality:",
                            "marks": [
                                {
                                    "type": "strong"
                                },
                                {
                                    "type": "textColor",
                                    "attrs": {
                                        "color": "#36b37e"
                                    }
                                }
                            ]
                        }
                    ]
                },
                {
                    "type": "orderedList",
                    "attrs": {
                        "order": 1
                    },
                    "content": [
                        {
                            "type": "listItem",
                            "content": [
                                {
                                    "type": "paragraph",
                                    "content": [
                                        {
                                            "type": "text",
                                            "text": ". . ."
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }

    return description


def create_ticket(summary, project, description, issue_type, priority):
    # Build Ticket
    issue = {'fields': {}}
    issue['fields']['summary'] = summary
    issue['fields']['issuetype'] = {'name': issue_type}
    issue['fields']['project'] = {'key': project}
    issue['fields']['description'] = description
    issue['fields']['labels'] = ['placeholder']
    issue['fields']['priority'] = {'name': priority}

    # Create ticket in Jira backlog
    url = f"{BASE_URL}/rest/api/3/issue"
    payload = json.dumps(issue)
    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=HEADERS,
        auth=AUTH
    )
    return response


if __name__ == "__main__":
    main()
