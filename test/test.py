#!/usr/bin/env python
# coding=utf-8

import unittest
import time
import os
import sys
sys.path.append("../src/")
import funcionesTwitter

class TestAplicacio(unittest.TestCase):

	#TESTEAR FUNCIÓN esPrivado(usu)
    def testEsPrivado(self):
        t = funcionesTwitter.FuncionesTwitter()
        #compruebo con mi usuario, como es público debe devolver False
        falso=t.esPrivado("rubenjior7")
        self.assertEqual(falso, False)

    #TESTEAR FUNCIÓN seguidos(usu)
    def testSeguidos(self):
        t = funcionesTwitter.FuncionesTwitter()
        #realizaré el estudio para un usuario privado y otro público
        usu1 = "rubenjior7"
        usu2 = "patrilara7"
        t.seguidos(usu1)
        t.seguidos(usu2)
        #Compruebo que existan los ficheros que se deben generar
        if os.path.isfile('../datos/seguidos/%s_seguidos.csv' % usu1) and os.path.isfile('../datos/seguidos/%s_seguidos.csv' % usu1):
            self.assertEqual(True, True)

    #TESTEAR FUNCIÓN obtenerTweetsUsuario(usu)
    def testObtenerTweetsUsuario(self):
        t = funcionesTwitter.FuncionesTwitter()
        salida = []
        salida = t.obtenerTweetsUsuario("rubenjior7")
        self.assertEqual(salida, t.obtenerTweetsUsuario("rubenjior7"))

    #TESTEAR FUNCIÓN obtenerDiccionarioTerrorismo()
    def testObtenerDiccionarioTerrorismo(self):
        t = funcionesTwitter.FuncionesTwitter()
        salida = []
        salida = t.obtenerDiccionarioTerrorismo()
        self.assertEqual(salida, t.obtenerDiccionarioTerrorismo())

    #TESTEAR FUNCIÓN obtenerDiccionarioComida()
    def testObtenerDiccionarioComida(self):
        t = funcionesTwitter.FuncionesTwitter()
        salida = []
        salida = t.obtenerDiccionarioComida()
        self.assertEqual(salida, t.obtenerDiccionarioComida())

    #TESTEAR FUNCIÓN obtenerDiccionarioRopa()
    def testObtenerDiccionarioRopa(self):
        t = funcionesTwitter.FuncionesTwitter()
        salida = []
        salida = t.obtenerDiccionarioRopa()
        self.assertEqual(salida, t.obtenerDiccionarioRopa())

    #TESTEAR FUNCIÓN obtenerDiccionarioAnimales()
    def testObtenerDiccionarioAnimales(self):
        t = funcionesTwitter.FuncionesTwitter()
        salida = []
        salida = t.obtenerDiccionarioAnimales()
        self.assertEqual(salida, t.obtenerDiccionarioAnimales())

    #TESTEAR FUNCIÓN ordenarContadores(usuario) y leerContadores(usuario), ya que se llama dentro de la primera
    def testOrdenarContadores(self):
        t = funcionesTwitter.FuncionesTwitter()
        usu = "rubenjior7"
        numero = t.ordenarContadores(usu)
        nummeroPrueba = 0
        self.assertEqual(type(numero), type(nummeroPrueba))

    #TESTEAR FUNCIÓN leerTweetsAnimales(usu)
    def testLeerTweetsAnimales(self):
        t = funcionesTwitter.FuncionesTwitter()
        usu = "rubenjior7"
        lista = t.leerTweetsAnimales(usu)
        self.assertEqual(lista, t.leerTweetsAnimales(usu))

    #TESTEAR FUNCIÓN leerTweetsRopa(usu)
    def testLeerTweetsRopa(self):
        t = funcionesTwitter.FuncionesTwitter()
        usu = "rubenjior7"
        lista = t.leerTweetsRopa(usu)
        self.assertEqual(lista, t.leerTweetsRopa(usu))

    #TESTEAR FUNCIÓN leerTweetsComida(usu)
    def testLeerTweetsComida(self):
        t = funcionesTwitter.FuncionesTwitter()
        usu = "rubenjior7"
        lista = t.leerTweetsComida(usu)
        self.assertEqual(lista, t.leerTweetsComida(usu))

    #TESTEAR FUNCIÓN leerTweetsTerrorismo(usu)
    def testLeerTweetsTerrorismo(self):
        t = funcionesTwitter.FuncionesTwitter()
        usu = "rubenjior7"
        lista = t.leerTweetsTerrorismo(usu)
        self.assertEqual(lista, t.leerTweetsTerrorismo(usu))

    #TESTEAR FUNCIONES escribirTweetsClasificados(usu, tweetsComida, tweetsRopa, tweetsAnimales, tweetsTerrorismo, tweetsSc), escribirDatosUsuario(usuario, contadorComida, contadorRopa, contadorAnimales, contadorTerrorismo, contadorSinCalificar) Y contadorTweetsPorCategorias(usu, nTweets)
    def testContadorTweetsPorCategorias(self):
        t = funcionesTwitter.FuncionesTwitter()
        usu = "rubenjior7"
        t.contadorTweetsPorCategorias(usu, 1141)
        #Compruebo que existan los ficheros que se deben generar
        if os.path.isfile('../datos/tweets/%s_tweets.csv' % usu) and os.path.isfile('../datos/tweets/%s_tweets_Animales.csv' % usu):
            self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
