from plantuml.API_Plant_UML import API_Plant_UML
from utils.Dev import Dev
from utils.Files import Files
from utils.Show_Img import Show_Img


class Test_Puml_dudes_experiments:

    # dudes
    def test_puml___dudes_creation(self):
        plantuml = API_Plant_UML()
        target_file = '/tmp/dudes-puml.png'
        puml = Files.contents('../dudes/puml/first-test.puml')

        #Dev.pprint(puml)
        png_file = plantuml.puml_to_png_using_lambda_function(puml,target_file)

        #Show_Img.from_path(png_file)
        #Dev.pprint(png_file)
