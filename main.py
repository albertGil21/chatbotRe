import os
import time
import google.generativeai as genai
from typing import Dict

api_key = "AIzaSyBcttk6LPhwvP-XoDsWoa_d4gLKC7n7GwI"
genai.configure(api_key=api_key)

class GeminiChatManager:
    def __init__(self):
        self.chat_sessions: Dict[str, genai.GenerativeModel.start_chat] = {}
        self.generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 50,
            "response_mime_type": "text/plain",
        }
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=self.generation_config,
        )
        
        # Cargar el archivo PDF una sola vez
        self.pdf_file = self.upload_to_gemini("reglamento.pdf", mime_type="application/pdf")
        self.wait_for_files_active([self.pdf_file])
        
        # Historial de entrenamiento inicial
        self.initial_history = [
            {
                "role": "user",
                "parts": [
                    self.pdf_file,
                    "comprende lo que está en ese pdf ",
                ],
            },
            {
                "role": "model",
                "parts": [
                    "The document you shared is a comprehensive guide for the admission process at the Universidad Nacional Mayor de San Marcos (UNMSM) in Peru for the 2024-II academic year. It covers a wide range of topics, including:\n\n**1.  Legal Framework:**\n    * The document begins by outlining the legal framework that governs the admission process, including the Peruvian Constitution, university laws, and relevant decrees.\n\n**2.  Glossary:**\n    * A glossary defines essential terms used throughout the document, such as \"Aspirante,\" \"Postulante,\" \"Vacante,\" \"Constancia de Ingreso,\" and \"Actos de Fraude.\"\n\n**3.  General Provisions:**\n    * This section describes the general organization of the university and its academic structure. It lists the different areas of study offered, including the schools of Medicine, Sciences, Engineering, Economics, Humanities, and Law.\n\n**4.  Admission Procedures:**\n    * The document details the various admission modalities available to prospective students, such as regular admission, first-place admission for secondary school graduates, admission for students with disabilities, admission for Indigenous students, and admission for athletes. \n    * It outlines the steps involved in each modality, from pre-registration and application to taking exams, completing medical evaluations, and receiving final admission documents.\n\n**5.  Exam Structure and Content:**\n    * The document provides detailed information about the general and special exams, including the format, sections, number of questions, subject areas, and time allotted. It also outlines the exam procedures and scoring criteria.\n\n**6.  Exonerations and Special Cases:**\n    * The document outlines various situations where students may be exempt from taking exams or may be eligible for special admission procedures, such as for diplomatic representatives, refugees, or those with certain academic backgrounds. \n\n**7.  Important Dates and Deadlines:**\n    * A detailed timeline outlines all important dates for the admission process, including deadlines for registration, pre-registration, exams, and receiving final admission documents.\n\n**8.  Ethics Guidelines:**\n    * A separate section dedicated to ethical guidelines emphasizes the importance of honesty, responsibility, and transparency during the admission process.\n\n**9.  Biosecurity Protocol:**\n    * The document emphasizes the importance of following biosecurity protocols during the admission process due to the COVID-19 pandemic.\n\n**10. Annexes:**\n    * The document concludes with annexes that provide further details and specific information, including:\n        * A list of schools and the number of available spots for each.\n        * A detailed pre-registration schedule for each school.\n        *  Instructions for completing the application form and uploading required documents.\n        *  The format for the official admission documents.\n        *  Ethical guidelines for applicants.\n        *  The structure of the general exam and special exams.\n        *  A model of the exam identification and answer sheet.\n        *  A timeline for receiving admission documents.\n        *  A sample certificate of original studies.\n        *  A map of the UNMSM campus.\n        *  A list of Banco de la Nación branches where admission fees can be paid.\n        *  A list of codes for specific admission fees.\n        *  Detailed content information for specific subject areas, such as mathematics, language, literature, psychology, history, geography, and economics.\n\nThe document is a comprehensive resource for prospective students who wish to apply to the UNMSM. It provides a clear, detailed, and user-friendly guide to the entire admission process, ensuring that applicants have a thorough understanding of their responsibilities and the procedures they need to follow. \n",
                ],
            },
            {
                "role": "user",
                "parts": [
                    "que se dice del articulo 2",
                ],
            },
            {
                "role": "model",
                "parts": [
                    "The article 2 of the document states that the admission process is in charge of the Oficina Central de Admisión (OCA), which was established by Resolution Rectoral N.°03028-R-04. The faculties and other university departments must provide the OCA with the resources and support it needs to carry out its work.\n",
                ],
            },
            {
                "role": "user",
                "parts": [
                    "tus respuestas no pueden estar en español?\n",
                ],
            },
            {
                "role": "model",
                "parts": [
                    "¡Lo siento!  Me olvidé de cambiar el idioma a español.  Voy a intentar hablar solo español a partir de ahora.  ¿Qué más te gustaría saber? \n",
                ],
            },
            {
                "role": "user",
                "parts": [
                    "quiero que cualquier pregunta de ahora en adelante sea respondida con informacion solo de los documentos que te doy\n",
                ],
            },
            {
                "role": "model",
                "parts": [
                    "¡Entendido! A partir de este momento, solo responderé con información de los documentos que me proporciones. \n\n¿Qué te gustaría saber?  😊 \n",
                ],
            },
            {
              "role": "user",
              "parts": [
                "cuando se fundó el perú",
              ],
            },
            {
              "role": "model",
              "parts": [
                "Lo siento, no puedo responder a esa pregunta. El documento que me proporcionaste no contiene información sobre la fecha de fundación del Perú. \n\n¿Te gustaría preguntarme algo sobre la información del documento? \n",
              ],
            },
            {
              "role": "user",
              "parts": [
                "quien es el presidente del peru",
              ],
            },
            {
              "role": "model",
              "parts": [
                "El documento no menciona el nombre del actual presidente del Perú.  \n\n¿Hay alguna otra pregunta que te gustaría hacer sobre la información contenida en el documento? \n",
              ],
            },
            {
              "role": "user",
              "parts": [
                "que dice el articulo 4 del reglamento",
              ],
            },
            {
              "role": "model",
              "parts": [
                "El artículo 4 del reglamento establece que si un estudiante quiere postular a la Escuela Profesional de Danza o Educación Física, tiene que pasar un examen médico y un examen de aptitud. Si pasa esos exámenes, puede inscribirse para la prueba general, siguiendo las instrucciones del artículo 35 del reglamento. \n",
              ],
            },
            {
              "role": "user",
              "parts": [
                "Que dice el articulo 3",
              ],
            },
            {
              "role": "model",
              "parts": [
                "El artículo 3 describe los diferentes tipos de modalidades de admisión disponibles para los estudiantes.  Aquí están las modalidades que menciona: \n\n* **Admisión Regular:** Esta modalidad es para estudiantes que han completado el ciclo de educación secundaria y quieren postular para estudios de pregrado. \n* **Admisión para estudiantes que se ubican entre los primeros puestos en su secundaria:** Esta modalidad es para estudiantes que se ubicaron entre los primeros puestos en su secundaria (colegio o instituto).\n* **Admisión para estudiantes con discapacidad:** Esta modalidad es para estudiantes con discapacidad.\n* **Admisión para estudiantes indígenas:** Esta modalidad es para estudiantes indígenas.\n* **Admisión para atletas:** Esta modalidad es para estudiantes que son atletas.\n\nEl artículo 3 también incluye las fechas límite para registrarse e inscribirse en cada una de las modalidades. \n\n\n",
              ],
            },
            {
              "role": "user",
              "parts": [
                "dime el articulo 5",
              ],
            },
            {
              "role": "model",
              "parts": [
                "El artículo 5 del reglamento indica que pueden postular por la modalidad de Educación Básica Regular (EBR) y Educación Básica Alternativa (EBA) las siguientes personas:\n\n* **Egresados de Educación Básica Regular (EBR)**\n* **Egresados de Educación Básica Alternativa (EBA)** \n",
              ],
            },
            {
              "role": "user",
              "parts": [
                "dime el articulo 3\n",
              ],
            },
            {
              "role": "model",
              "parts": [
                "El artículo 3 del reglamento describe el proceso de admisión como un proceso que se divide en dos etapas: \n\n* **Admisión 2024-I:** Esta etapa se realiza en el segundo semestre del 2023. \n* **Admisión 2024-II:** Esta etapa se realiza en el primer semestre del 2024. \n\nLos estudiantes que ingresen en cualquiera de estas dos etapas empezarán sus clases en el primer periodo académico del 2024. \n",
              ],
            }
            
        ]

    def upload_to_gemini(self, path, mime_type=None):
        file = genai.upload_file(path, mime_type=mime_type)
        print(f"Uploaded file '{file.display_name}' as: {file.uri}")
        return file

    def wait_for_files_active(self, files):
        print("Waiting for file processing...")
        for name in (file.name for file in files):
            file = genai.get_file(name)
            while file.state.name == "PROCESSING":
                print(".", end="", flush=True)
                time.sleep(10)
                file = genai.get_file(name)
            if file.state.name != "ACTIVE":
                raise Exception(f"File {file.name} failed to process")
        print("...all files ready")
        print()

    def create_new_session(self, session_id: str):
        """Crear una nueva sesión de chat para un usuario específico."""
        if session_id not in self.chat_sessions:
            # Usar el historial inicial para cada nueva sesión
            self.chat_sessions[session_id] = self.model.start_chat(history=self.initial_history)
            return True
        return False

    def get_session(self, session_id: str):
        """Obtener una sesión existente o crear una nueva si no existe."""
        if session_id not in self.chat_sessions:
            self.create_new_session(session_id)
        return self.chat_sessions[session_id]

    def send_message(self, session_id: str, message: str) -> str:
        """Enviar un mensaje a una sesión específica."""
        try:
            chat_session = self.get_session(session_id)
            response = chat_session.send_message(message)
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"

    def delete_session(self, session_id: str) -> bool:
        """Eliminar una sesión de chat."""
        if session_id in self.chat_sessions:
            del self.chat_sessions[session_id]
            return True
        return False