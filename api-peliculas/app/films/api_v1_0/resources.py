from flask import request, Blueprint
from flask_restful import Api, Resource

from .schemas import FilmSchema
from ..models import Film, Actor

from ...common.error_handling import ObjectNotFound, AppErrorBaseClass


films_v1_0_bp = Blueprint('films_v1_0_bp', __name__)

film_schema = FilmSchema()

api = Api(films_v1_0_bp)


class FilmListResource(Resource):
    def get(self):
        films = Film.get_all()
        result = film_schema.dump(films, many=True)
        return result
    
    def post(self):
        data = request.get_json()
        film_dict = film_schema.load(data)
        film = Film(title=film_dict['title'],
        length=film_dict['length'],
        year=film_dict['year'],
        director=film_dict['director'])
        
        for actor in film_dict['actors']:
            film.actors.append(Actor(actor['name']))

        film.save()
        resp = film_schema.dump(film)
        return resp, 201
    
    
class FilmResource(Resource):
    def get(self, film_id):
        film = Film.get_by_id(film_id)
        if film is None:
            # Si la película no se encuentra, lanza la excepción ObjectNotFound
            raise ObjectNotFound(f"La película con ID {film_id} no fue encontrada")
        resp = film_schema.dump(film)
        return resp


api.add_resource(FilmListResource, '/api/v1.0/films/', endpoint='film_list_resource')
api.add_resource(FilmResource, '/api/v1.0/films/<int:film_id>', endpoint='film_resource')