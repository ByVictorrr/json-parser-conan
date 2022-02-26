from conans import ConanFile, AutoToolsBuildEnvironment, tools

class HelloConan(ConanFile):

    name="json-parser"
    version='1.0.0'
    exports_sources="json-parser/*"

    def source(self):
        git = tools.Git()
        git.clone("https://github.com/json-parser/json-parser.git", "master")

    def build(self):
         autotools = AutoToolsBuildEnvironment(self, win_bash=tools.os_info.is_windows)
         tools.dos2unix("configure")
         tools.dos2unix("configure.ac")
         tools.dos2unix("Makefile.in")
         autotools.configure()

         tools.dos2unix("Makefile")
         autotools.make()



    def package(self):
        self.copy("*.h", dst="include/json-parser/")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib")
        self.copy("*.a", dst="lib")



