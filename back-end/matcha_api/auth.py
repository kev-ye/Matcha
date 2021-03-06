from flask import Blueprint
from flask_jwt_extended import jwt_required
from flask_restful import Api, Resource

import matcha_api.services.auth_s as service

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')
api = Api(auth_bp)


class SignUp(Resource):
	# noinspection PyMethodMayBeStatic
	def post(self):
		return service.handle_signup()


class SignIn(Resource):
	# noinspection PyMethodMayBeStatic
	def post(self):
		return service.handle_signin()


class RefreshToken(Resource):
	@jwt_required(refresh=True)
	def post(self):
		return service.handle_refresh()


class IsLogin(Resource):
	@jwt_required()
	def get(self):
		return service.handle_is_login()


api.add_resource(SignUp, '/signup')
api.add_resource(SignIn, '/signin')
api.add_resource(IsLogin, '/islogin')
api.add_resource(RefreshToken, '/refresh')
