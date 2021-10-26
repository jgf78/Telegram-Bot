# Importamos las librerías necesarias
from telegram.ext import Updater, MessageHandler, CommandHandler, InlineQueryHandler, Filters

# Método que imprimirá por pantalla la información que reciba
def listener(bot, update):
    print("Holaaaa")

# Método que utilizaremos para cuando se mande el comando de "enlaces"
def trust(update, context):
    update.message.reply_text('Este es el enlace de registro de Trust Investing: ' + 'https://bit.ly/3oIizYR')
def sotavento(update, context):
    update.message.reply_text('Este es el enlace de registro de Sotavent0: ' + 'https://bit.ly/3sUpsco')
def pi(update, context):
    update.message.reply_text('Este es el enlace de registro de Pi: ' + 'https://bit.ly/3p0X35h')  
def minex(update, context):
    update.message.reply_text('Este es el enlace de registro de Minexcorp: ' + 'https://bit.ly/3yaZUJO')
def gdollar(update, context):
    update.message.reply_text('Este es el enlace de registro de GoodDollar: ' + 'https://bit.ly/30sEkFT' )          
    

def main():
    # Creamos el Updater, objeto que se encargará de mandarnos las peticiones del bot asignando el token
    updater = Updater(token='2065671113:AAG__dMnay2bpQS7tO16P9NZ7AMXYypcY0k', use_context=True)

    # Cogemos el Dispatcher, en el cual registraremos los comandos del bot y su funcionalidad
    dispatcher = updater.dispatcher

    # Ahora registramos cada método a los comandos necesarios
    dispatcher.add_handler(CommandHandler("trustinvesting", trust))
    dispatcher.add_handler(CommandHandler("sotavento", sotavento))
    dispatcher.add_handler(CommandHandler("pi", pi))
    dispatcher.add_handler(CommandHandler("minexcorp", minex))
    dispatcher.add_handler(CommandHandler("gooddollar", gdollar))

    # Y comenzamos la ejecución del bot a las peticiones
    updater.start_polling()
    updater.idle()

# Llamamos al método main para ejecutar lo anterior
if __name__ == '__main__':
    main()