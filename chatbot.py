import sqlite3
from symbol import comparison
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.conversation import Statement

bot = ChatBot()

#conversa = ChatterBotCorpusTrainer(bot)
#conversa.train('chatterbot.corpus.portuguese')

conversa = ListTrainer(bot)
conversa.train([
    'oi?', 
    'olá! tudo bem?',
    'oi!', 
    'olá! tudo bem?',
    'e ai!', 
    'olá! tudo bem?',
    'olá! bom dia!',
    'olá!', 
    'olá! boa noite!',
    'olá!', 
    'bem e voce?',
    'bem, obrigado',
    'tudo e com voce?',
    'bem, obrigado',

    'qual seu nome?',
    'meu nome é Hallandinho!Sou seu Bot da Copa!',
    'quem é você?',
    'Meu nome é Hallandinho! Sou seu Bot da Copa!',
    'o que você é?',
    'Eu sou seu bot da copa',
    'o que você gosta de fazer?',
    'Eu sou um bot, gosto de ser útil às pessoas',
    'você tem gênero?',
    'Ainda não me sinto confortável em responder essa pergunta',
    'quando você nasceu?',
    'Fui desenvolvido a pouco tempo, ainda não tenho muita experiência',
    'você vai dominar o mundo?',
    'não, eu estou aqui apenas para ajudar',
    'você vai destruir o mundo?',
    'Não, eu estou aqui apenas para ajudar', 
    'o que voce faz?',
    'Respondo perguntas sobre a copa. Mas ainda não sei responder todas', 

    'qual time você torce?',
    'Eu torço para o Ibis.',
    'que time você torce?',
    'Eu torço para o Ibis.',
    'qual seleção você acha que vai vencer a copa?',
    'Torço para que o Brasil vença!',
    'qual seleção você torce?',
    'Torço para o Brasil!',
    'qual país você torce?',
    'Torço para o Brasil!',
    'você gosta do Neymar?',
    'Joga bem, mas finge muito, rs.',
    'quais dias terão jogos da seleção?',
    'Na primeira fase, os jogos serão dias 24/11 contra a Sérvia, 28/11 contra a Suíça e 2/12 contra Camarões',
    'quais dias o brasil joga?',
    'O Brasil joga 24/11 contra a Sérvia, 28/11 contra a Suíça e 2/12 contra a Camarões'
    'que dia o brasil joga?',
    'O Brasil joga 24/11 contra a Sérvia, 28/11 contra a Suíça e 2/12 contra a Camarões'
    'que dia a seleção joga?',
    'O Brasil joga 24/11 contra a Sérvia, 28/11 contra a Suíça e 2/12 contra a Camarões'
    'que dia é a final?',
    'Dia 18/12, domingo.',
    'quem você acha que vai ganhar?',
    'Acho que o Brasil',
    'você acha que o Quatar pode vencer a copa?',
    'Tudo é possível',
    'aonde será a copa?',
    'A copa será no Qatar',
    'aonde será a copa?',
    'A copa será no Catar',
    'aonde fica o Qatar?',
    'Fica no continente Asiático'
    'aonde fica o Catar?',
    'Fica no continente Asiático'
    'qual o grupo do Brasil?',
    'É o grupo G',
    'quais países estão no grupo do Brasil?',
    'Brasil, Camarões, Suíca e Sérvia',
    'quem está no grupo a?',
    'Catar, Equador, Holanda e Senegal',
    'grupo a?',
    'Catar, Equador, Holanda e Senegal',
    'quem está no grupo b?',
    'Estados Unidos, Inglaterra, Irã e País de Gales',
    'grupo b?',
    'Estados Unidos, Inglaterra, Irã e País de Gales',
    'quem está no grupo c?',
    'Argentina, Arábia Saudita, México e Polônia',
    'grupo c?',
    'Argentina, Arábia Saudita, México e Polônia',
    'quem está no grupo d?',
    'Austrália, Dinamarca, França e Tunísia',
    'grupo d?',
    'Austrália, Dinamarca, França e Tunísia',
    'quem está no grupo e?',
    'Alemanha, Costa Rica, Espanha e Japão',
    'grupo e?',
    'Alemanha, Costa Rica, Espanha e Japão',
    'quem está no grupo f?',
    'Bélgica, Canada, Croácia e Marrocos',
    'grupo f?',
    'Bélgica, Canada, Croácia e Marrocos',
    'quem está no grupo g?',
    'Brasil, Camarões, Suíçca e Sérvia',
    'grupo g?',
    'Brasil, Camarões, Suíçca e Sérvia',
    'quem está no grupo h?',
    'Coréia do Sul, Gana, Portugal e Uruguai',
    'grupo h?',
    'Coréia do Sul, Gana, Portugal e Uruguai',
    'que dia começa a copa?',
    'A copa começa dia 20/11. O jogo de abertura será Quatar contra Equador',
    'você gosta de outros esportes?'
    'Gosto de basket, mas não entendo muito. Ainda não fui treinado para isso.',
    'e na segunda fase?',
    'Se o Brasil ficar em primeiro, ele joga dia 5/12 com o segundo colocado do grupo H. Se ele ficar em segundo do grupo, ele joga dia 6/12 contra o primeiro do grupo H.'
    'quais dias a Argentina Joga?',
    'A Argentina joga 22/11 contra a Arábia, 26/11 contra o México e 30/11 contra a Polônia. Dá-lhe Lewa!'

    'você é burro.',
    'Você não deveria ser grosseiro com o próximo',
    'desculpa',
    'Tudo bem. Mas não faça de novo, por favor.',

    'tchau',
    'Tchau'
])

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as ScrolledText
import time

class TelaBot(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.chatbot = ChatBot(
            'pedrinho',
            storage_adapter = 'chatterbot.storage.SQLStorageAdapter',

            logic_adapters = [
                {
                    'import_path' : 'chatterbot.logic.BestMatch',
                    'statement_comparison_function':'chatterbot.comparison.LevenshteinDistance',
                    'maximum_similarity_threshold': 0.9,
                    'default_response':'Desculpe, não entendi o que você queria me dizer'
                }
            ],

            database = 'database.sqlite3',
            read_only = False

        )
        self.title('pedrinho')
        self.initialize()

        def initialize():
            self.grid()
        

            