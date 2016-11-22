SECRET_KEY = ":-)"

INSTALLED_APPS = [
	"tests",
]

DATABASES = {
	"default": {
		"ENGINE": "django.db.backends.sqlite3",
		"NAME": ":memory:",
		# "TEST_NAME": ":memory:",
	}
}
