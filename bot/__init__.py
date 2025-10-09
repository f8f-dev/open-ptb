from telegram.ext import Application


bot_instance = Application.builder().token("TOKEN").build()


__all__ = ["bot_instance"]
