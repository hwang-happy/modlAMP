import unittest
from os.path import abspath, join

from ..wetlab import CD


class TestCD(unittest.TestCase):
	cd = CD(join(abspath('.'), 'modlamp/tests/files'), 180, 260, amide=True)

	def test_init(self):
		self.assertIsNotNone(self.cd.filenames)
		self.assertIsInstance(self.cd.filenames[0], basestring)

	def test_read_header(self):
		self.assertEqual(self.cd.sequences[0], 'KLLKLLKKLVGALG')
		self.assertEqual(self.cd.sequences[1], 'GLFDIVKKVLKLLK')
		self.assertEqual(self.cd.conc_umol[0], 33.)
		self.assertAlmostEqual(self.cd.conc_mgml[0], 0.04926938, 5)
		self.assertAlmostEqual(self.cd.meanres_mw[0], 114.84704615, 4)

	def test_molar_ellipticity(self):
		self.cd.calc_molar_ellipticity()
		self.assertAlmostEqual(self.cd.molar_ellipticity[0][0, 1], -1172778.7878787878, 5)
		
	def test_meanres_ellipticity(self):
		self.cd.calc_meanres_ellipticity()
		self.assertAlmostEqual(self.cd.meanres_ellipticity[0][38, 1], -1990.3473193473196, 5)
		
	def test_helicity(self):
		self.cd.calc_meanres_ellipticity()
		self.cd.helicity()
		self.assertEqual(float(self.cd.helicity_values.iloc[1]['Helicity']), 79.68)
		
if __name__ == '__main__':
	unittest.main()
