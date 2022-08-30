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
    # app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
    # app.config['MAIL_PORT'] = 2525
    # app.config['MAIL_USERNAME'] = 'd832590766d685'
    # app.config['MAIL_PASSWORD'] = '5e3b44ef41e047'
    # app.config['MAIL_USE_TLS'] = True
    # app.config['MAIL_USE_SSL'] = False


    # setup for real-world usage
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'games.grotto.uk@gmail.com'
    app.config['MAIL_PASSWORD'] = 'joqctptdnzmymoay'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    return Mail(app)
