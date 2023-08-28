import openai

openai.api_key = "API-KEY-OPENAI"

def generer_code_html(sujet):
    prompt = f"Create a website in html css and js in a single file, you must do at least 50 lines of code, the site must be visually beautiful so choose the right style in the css. Encode it in UTF-8. Here is the subject of the site to be created:{sujet}."
    response = openai.Completion.create(
        engine="text-davinci-003",  
        prompt=prompt,
        max_tokens=4000
    )
    code_html = response.choices[0].text.strip()
    return code_html

def enregistrer_dans_fichier(code_html, dossier):
    chemin_fichier = f"{dossier}/index.html"
    with open(chemin_fichier, "w") as fichier:
        fichier.write(code_html)
    print(f"HTML code saved in {chemin_fichier}")

def main():
    sujet = input("What topic do you want for your website? ")
    code_html = generer_code_html(sujet)

    dossier_projet = "generate"
    enregistrer_dans_fichier(code_html, dossier_projet)

if __name__ == "__main__":
    main()
