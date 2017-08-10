import unittest, re, subprocess

class TestEnv(unittest.TestCase):

	def test_java(self):
		version = subprocess.Popen(['java', '-version'], stderr=subprocess.PIPE).communicate()[1]
		pattern = '\"(\d+\.\d+\.\d+_\d+).*\"'
		shortVersion = re.search(pattern, version).groups()[0]
		print('  CHECK java version =', shortVersion)
		self.assertEqual(shortVersion, '1.8.0_131')
		
	def test_sbt(self):
		cmd = "sbt sbtVersion"
		version = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]
		pattern = '(\d+\.\d+\.\d+)'
		shortVersion = re.search(pattern, version).groups()[0]
		print('  CHECK sbt version =', shortVersion)
		self.assertEqual(shortVersion, '0.13.15')
		
if __name__ == '__main__':
	unittest.main()
