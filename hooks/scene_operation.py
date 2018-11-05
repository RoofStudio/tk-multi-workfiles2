#############################################
import os
import imp

import tank
from tank import Hook
from tank import TankError



class SceneOperation( Hook ):
	"""
	Hook called to perform an operation with the
	current scene
	"""

	def execute(self, operation, file_path, context, parent_action, file_version, read_only, **kwargs):
		# get the engine name from the parent object (app/engine/etc.)
		engine = self.parent.engine

		# load contants
		constants = imp.load_source( "constants", os.path.join(os.path.dirname(__file__),'constants.py') )

		# set pre publish operations path
		PYC_PATH = constants.HOOK_PATH.format( hook_file= ("scene_operation_"+engine.instance_name+"_OP.pyc") )
		if not os.path.exists( PYC_PATH ):
			raise TankError( "Unable to perform scene_operations at %s for unhandled engine %s" % (PYC_PATH, engine.name) )

		# import module
		mod = imp.load_compiled('scene_operations', PYC_PATH)

		results = None

		if operation == "current_path":
			results = mod.get_current_scene_path()

		elif operation == "open":
			results = mod.open( file_path )

		elif operation == "save":
			results = mod.save( file_path )

		elif operation == "save_as":
			results = mod.save_as( file_path )

		elif operation == "reset":
			results = mod.new_file( context )


		return results
