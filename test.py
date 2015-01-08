import unittest, os
from robot import a_star
class A_starTest(unittest.TestCase):
	filepath = os.path.join(os.path.split(os.path.realpath(__file__))[0],'test1')
	def setUp(self):
		pass

	def test_set_point(self):
		star = a_star(self.filepath)
		self.assertEqual(star.set_point((0,0),(5,5)),True)
		self.assertEqual(star.set_point((-1,0),(5,5)),False)

	def test_readmap(self):
		star = a_star(self.filepath)
		self.assertEqual(star.readmap(self.filepath),True)

	def test_h(self):
		star = a_star(self.filepath)
		star.set_point((0,0),(5,5))
		self.assertEqual(type(star.h(2,3)),int)

	def test_setvalue(self):
		star = a_star(self.filepath)
		star.set_point((0,0),(5,5))
		self.assertEqual(star.setvalue((1,1),1,"l"),True)

	def test_viewpoint(self):
		star = a_star(self.filepath)
		star.set_point((1,1),(5,5))
		self.assertRaises(TypeError,star.viewpoint,0,0)

	def test_findminipoint(self):
		star = a_star(self.filepath)
		star.set_point((1,1),(5,5))
		self.assertEqual(type(star.findminipoint()),tuple)

	def test_get_path(self):
		star = a_star(self.filepath)
		star.set_point((2,2),(3,4))
		star.running()
		self.assertEqual(type(star.get_path()),list)

	def test_running(self):
		star = a_star(self.filepath)
		star.set_point((2,2),(3,4))
		self.assertEqual(type(star.running()),list)

if __name__ == '__main__':
	unittest.main()