"""Small syntax examples for the cross-language section of the video."""

PYTHON_OBSERVER = '''
publisher.subscribe(email_subscriber)
publisher.publish(issue)
'''

JAVA_OBSERVER = '''
publisher.addListener(emailSubscriber);
publisher.notifyListeners(issue);
'''

JAVASCRIPT_OBSERVER = '''
publisher.on("issuePublished", listener);
publisher.emit("issuePublished", issue);
'''
