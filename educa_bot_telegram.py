# -*- coding: utf-8 -*-

import requests
from telegram.ext import Updater, CommandHandler,CallbackQueryHandler,MessageHandler, Filters,RegexHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

class educasp():

  def main(self):
        try:
            ## validação do token 
            token_telegram = 'seu token'
            updater = Updater(token = token_telegram, use_context = True)

            ## chamando o welcome
            ud = updater.dispatcher
            ud.add_handler(CommandHandler('iniciar', self.welcome))
            ud.add_handler(CallbackQueryHandler(self.main_menu, pattern = 'menu'))
            ud.add_handler(CallbackQueryHandler(self.button))
            ud.add_handler(CommandHandler('ajuda', self.ajuda))
            
            ## continue a rodar
            updater.start_polling()
            updater.idle()
            
        except Exception as e:
            print(str(e))

  def welcome(self,update,context):

        try:
            ## hello user!
            username = update.message.from_user.username
            firstName = update.message.from_user.first_name
            lastName = update.message.from_user.last_name
            message = 'Olá, ' + firstName + '!'
            context.bot.send_message(chat_id = update.effective_chat.id, text=message)
            
            #menu
            update.message.reply_text('Escolha uma das opções:', reply_markup = self.menu_keyboard_principal())
            
        except Exception as e:
            print ('Exception babe ' + str(e))
  
  
  
  
  ### keyboards
  def menu_keyboard_principal(self):
      menu = [[ InlineKeyboardButton('O que é o EducaSP?', callback_data= '0')],
                [ InlineKeyboardButton('Quais cursos posso fazer?', callback_data='1')],
                [ InlineKeyboardButton('Como me inscrevo?', callback_data='2')],
                [ InlineKeyboardButton('Esqueci a senha', callback_data='3')],
                [ InlineKeyboardButton('Certificados', callback_data='4')],
                [ InlineKeyboardButton('Quer saber mais? (FAQ)', callback_data='5', url= 'https://www.fuvest.br/educasp-usp/')]]

      reply = InlineKeyboardMarkup(menu)
      return reply        
      
      
  def menu_keyboard_secundario(self):

      volte_menu = [[ InlineKeyboardButton('Menu principal', callback_data= 'menu')]]
      
      reply2 = InlineKeyboardMarkup(volte_menu)
      return reply2
  

  ### Ações do menu
  def main_menu(self, update, context):

      query = update.callback_query
      message = 'Escolha uma das opções:'
      context.bot.edit_message_text(chat_id=query.message.chat_id,
                                    message_id=query.message.message_id,
                                    text=message,
                                    reply_markup= self.menu_keyboard_principal())
  
      
  def button(self, update,context):

      query = update.callback_query

      if query.data == '0':
          message = '*O que é o EducaSP?*\n\n   A Universidade de São Paulo (USP) objetiva com o programa USP EducaSP contribuir com a formação de estudantes do Ensino Médio por meio da oferta de cursos de formação complementar, fortalecendo a conexão desses estudantes com o Ensino Superior.\n   O programa é fruto da parceria entre a USP, FUVEST e Secretaria da Educação do Estado de São Paulo e atenderá, exclusivamente, estudantes regularmente matriculados no Ensino Médio das escolas públicas estaduais do Estado de São Paulo.'
          context.bot.edit_message_text(chat_id=query.message.chat_id,
                                        message_id=query.message.message_id,
                                        text= message,
                                        reply_markup = self.menu_keyboard_secundario())
      
      elif query.data == '1':

          message = " Os cursos oferecidos atualmente são: \n1) Astrobiologia \n2) Apps e jogos \n3) Decifrando seu dinheiro \n4) Fotografia \n5) Expedição literaria \n6) Lasers, luzes e cores \n7) Quero engenhar! \n8) Negociações internacionais \n9) Robótica  \n10) Super tecnologias "
          context.bot.edit_message_text(chat_id=query.message.chat_id,
                                        message_id=query.message.message_id,
                                        text= message,
                                        reply_markup = self.menu_keyboard_secundario())
          
      elif query.data == '2':

          message = " Entre no site: https://www.fuvest.br/cuco-competicao-usp-de-conhecimentos e faça seu cadastro! Os cursos são grátis!"
          context.bot.edit_message_text(chat_id=query.message.chat_id,
                                        message_id=query.message.message_id,
                                        text= message,
                                        reply_markup = self.menu_keyboard_secundario())

      elif query.data == '3':
          message = "Seu login é o seu CPF e a senha é o seu RA"
          context.bot.edit_message_text(chat_id=query.message.chat_id,
                                        message_id=query.message.message_id,
                                        text= message,
                                        reply_markup = self.menu_keyboard_secundario())
          
      elif query.data == '4':
          message = "Para obter o certificado, basta acessar https://www.fuvest.br/educasp-usp/ e clicar em Área do Candidato. Em seguida, entre na plataforma com seu e-mail ou CPF e senha. Após entrar na plataforma, na aba Meus Exames, clique no curso ofertado no semestre passado e em Resultados. "
          context.bot.edit_message_text(chat_id=query.message.chat_id,
                                        message_id=query.message.message_id,
                                        text= message,
                                        reply_markup = self.menu_keyboard_secundario())

  def ajuda(self, update, context):

    update.message.reply_text("Digite /start para iniciar o robô.")


if __name__ == "__main__":
      educasp().main()
