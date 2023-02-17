"""
Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(DesktopBot):
    def action(self, execution=None):
        # Uncomment to silence Maestro errors when disconnected
        # if self.maestro:
        #     self.maestro.RAISE_NOT_CONNECTED = False

        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        self.browse("https://www.instagram.com")
        
        if not self.find( "carregou", matching=0.97, waiting_time=10000):
            self.not_found("carregou")
        
        if not self.find( "pesquisar", matching=0.97, waiting_time=10000):
            self.not_found("pesquisar")
        self.click()
        
        if not self.find( "pesquisar alguem", matching=0.97, waiting_time=10000):
           self.not_found("pesquisar alguem")
        self.click()
       
        
        self.paste("lebron")
        
        if not self.find( "achou", matching=0.97, waiting_time=10000):
            self.not_found("achou")
        self.click()
        
        if not self.find( "mandar mensagem", matching=0.97, waiting_time=10000):
            self.not_found("mandar mensagem")
        self.click()
        

        # self.maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()

