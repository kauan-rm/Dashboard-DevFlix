$env:FLASK_APP="manage.py"
$env:SQLALCHEMY_DATABASE_URI="mysql://root@localhost:3306/devflix"
$env:SQLALCHEMY_TRACK_MODIFICATIONS=0
$env:SECRET_KEY="TY744dZYfqKFCgfcLExo6GEppE5UZWi0"
$env:MAIL_SERVER='smtp-mail.outlook.com'
$env:MAIL_PORT='587'
$env:MAIL_USE_TLS=1
$env:MAIL_USE_SSL=0
$env:MAIL_USERNAME="devflix@hotmail.com"
$env:MAIL_PASSWORD="Trembala"
$env:FLASKY_MAIL_SUBJECT_PREFIX = 'Confirmação de Email'

$env:FLASK_DEBUG=1