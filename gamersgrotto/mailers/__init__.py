from flask_mail import Mail


def mail_config(app):
    """use service such as mailtrap.io to get your own details!

    Note that mailtrap literally traps the mail for testing purposes!
    Don't panic that the email doesn't get the end recipient if using this service.
    The email will arrive in your mailtrap inbox, stating the intended recipient address.

    If you want to use a 'real' account for this, don't choose Gmail as it has
    security features that need to be turned off to allow this functionality.
    """

    # Used my own mailtrap to recieve emails to see if it was working.
    app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
    app.config['MAIL_PORT'] = 2525
    app.config['MAIL_USERNAME'] = '734309792e682e'
    app.config['MAIL_PASSWORD'] = '98d1a31b431068'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False

    # app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
    # app.config['MAIL_PORT'] = 2525
    # app.config['MAIL_USERNAME'] = '4e5faaae935cfc'
    # app.config['MAIL_PASSWORD'] = 'e621df0a5cc7d7'
    # app.config['MAIL_USE_TLS'] = True
    # app.config['MAIL_USE_SSL'] = False

    return Mail(app)
