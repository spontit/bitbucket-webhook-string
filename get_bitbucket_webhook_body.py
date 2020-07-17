def get_bitbucket_webhook_body(payload):
    result = str()

    if payload.get('actor'):
        actor = payload['actor']
        if actor.get('display_name'):
            result += "Actor: " + str(actor['display_name']) + "\n"

    if payload.get('repository'):
        repository = payload['repository']
        repo_name = repository.get('name')
        if repo_name:
            result += "Repository: " + str(repo_name) + "\n"

        project = payload.get('project')
        if project:
            project_name = project.get('name')
            if project_name:
                result += "Project Name: " + str(project_name) + "\n"

    if payload.get('push'):
        push = payload['push']
        result += "New Push: "
        changes = push.get('changes', list())
        if type(changes) == list:
            for change in changes:
                commits = change.get('commits', list())
                if type(commits) == list:
                    for commit in commits:
                        author_display_name = commit.get('author', dict()).get('user', dict()).get('display_name')
                        date = commit.get('date')
                        commit_url = commit.get('links', dict()).get('self', dict()).get('href', dict())
                        commit_message = commit.get('message')

                        result += "\n\tNew Commit"
                        if author_display_name:
                            result += "\n\t\tAuthor: " + str(author_display_name)
                        if date:
                            result += "\n\t\tDate: " + str(date)
                        if commit_message:
                            result += "\n\t\tMessage: " + str(commit_message)
                        if commit_url:
                            result += "\n\t\tCommit URL: " + str(commit_url)

    return result
