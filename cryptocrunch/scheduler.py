from flask_apscheduler import APScheduler as _BaseAPScheduler


class APScheduler(_BaseAPScheduler):
    """
    Ensure that the scheduled jobs are running with the flask app context
    """
    def run_job(self, id, jobstore=None):
        with self.app.app_context():
            super().run_job(id=id, jobstore=jobstore)


scheduler = APScheduler()
